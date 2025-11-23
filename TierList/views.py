from datetime import datetime
from django.shortcuts import render
import json
from django.shortcuts import redirect

# Create your views here.

from django.contrib import admin
from .models import Ranking, Image
from django.http import HttpResponse
from .forms import TierListForm

# THIS FUNC IS WIP
def maker(request):
    if request.method == "POST":
        form = TierListForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Process the valid form data
            title = form.cleaned_data['title']
            ranking_data = form.cleaned_data['ranking_data']
            ranking_type = request.POST.get('ranking_type')
            # Save the ranking data to the database or perform other actions
            ranking = Ranking.objects.create(
                list_name=title,
                creation_date=datetime.now(),
                tier_config=ranking_data,
                type=ranking_type
            )

            # image_data is a list of base64 strings
            import base64
            from django.core.files.base import ContentFile
            image_data_list = form.cleaned_data['image_data']
            for idx, img_b64 in enumerate(image_data_list):
                # Remove header if present
                if "," in img_b64:
                    header, img_b64 = img_b64.split(",", 1)
                img_file = ContentFile(base64.b64decode(img_b64), name=f"uploaded_{idx}.png")
                Image.objects.create(ranking=ranking, image=img_file)

            return redirect('detail', ranking_id=ranking.id)
    else:
        form = TierListForm()
    return render(request, 'maker.html', {'form': form})

def index(request):
    return render(request, 'home.html')

def new(request):
    return render(request, 'new.html')

def config(request):
    return render(request, 'config.html')

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


def create(request, ranking_id):
    ranking = Ranking.objects.get(id=ranking_id)
    images = ranking.images.all()
    context = {
        'ranking': ranking,
        'images': images,
    }
    return render(request, 'create.html', context)