from datetime import datetime
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, render
import json
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from .models import Ranking, Image
from django.http import HttpResponse

from .forms import ImageUploadForm, TierListForm

def maker(request):
    return render(request, 'maker.html')

# {"rows": {"S": [], "A": [], "F": ["http://127.0.0.1:8000/static/TierList/greencrewpng.png"]}, "unassigned": ["http://127.0.0.1:8000/static/TierList/blackcrewpng.png", "http://127.0.0.1:8000/static/TierList/bluecrewpng.png", "http://127.0.0.1:8000/static/TierList/redcrewpng.png"]}


# THIS FUNC IS WIP
@login_required
def config(request):
    if request.method == "POST":
        form = TierListForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            ranking_data = {"rows": {0: { "images": [], "color": '#C0C0C0', "name": 'S' },
                                     1: { "images": [], "color": '#C0C0C0', "name": 'A' },
                                     2: { "images": [], "color": '#C0C0C0', "name": 'B' },
                                     3: { "images": [], "color": '#C0C0C0', "name": 'C' },
                                     4: { "images": [], "color": '#C0C0C0', "name": 'D' },
                                     5: { "images": [], "color": '#C0C0C0', "name": 'F' }
                            }, "unassigned": []}
            ranking = Ranking.objects.create(
                list_name=title,
                creation_date=datetime.now(),
                tier_config=ranking_data,
                author=request.user
            )
            # Get all uploaded images
            images = request.FILES.getlist('images')
            for image in images:
                Image.objects.create(ranking=ranking, image=image)
            return redirect('edit', ranking_id=ranking.id)
    else:   
        form = TierListForm()
    return render(request, 'config.html', {'form': form})

def index(request):
    return render(request, 'home.html')

def new(request):
    return render(request, 'new.html')

@login_required
def dashboard(request):
    rankings = Ranking.objects.filter(author=request.user)
    return render(request, 'dashboard.html', {'rankings': rankings})

def discover(request):
    rankings = Ranking.objects.all()
    return render(request, 'discover.html', {'rankings': rankings})

def detail(request, ranking_id):
    ranking = Ranking.objects.get(id=ranking_id)
    images = ranking.images.all()
    context = {
        'ranking': ranking,
        'images': images,
    }
    return render(request, 'detail.html', context)

@login_required
def edit(request, ranking_id):
    instance = get_object_or_404(Ranking, pk=ranking_id)

    if request.user != instance.author:
        # Handle unauthorized access (e.g., redirect to detail page or show an error)
        return redirect('detail', ranking_id=ranking_id)

    if request.method == "POST":
        tier_config_json = request.POST.get('tier_config')
        ranking = Ranking.objects.get(id=ranking_id)
        ranking.tier_config = json.loads(tier_config_json)
        ranking.save()
        return redirect('detail', ranking_id=ranking.id)
    else:
        ranking = Ranking.objects.get(id=ranking_id)
        images = ranking.images.all()
        context = {
            'ranking': ranking,
            'images': images,
        }
        return render(request, 'edit.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Or to your desired page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    return render(request, 'login.html')

def login(request):
    return render(request, 'logout.html')