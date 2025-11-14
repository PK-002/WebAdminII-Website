from datetime import datetime
from django.shortcuts import render
import json
from django.shortcuts import redirect

# Create your views here.

from django.contrib import admin
from .models import Ranking
from django.http import HttpResponse
from .forms import TierListForm


def maker(request):
    if request.method == "POST":
        form = TierListForm(request.POST)
        if form.is_valid():
            # Process the valid form data
            title = form.cleaned_data['title']
            ranking_data = form.cleaned_data['ranking_data']
            # Save the ranking data to the database or perform other actions
            ranking = Ranking.objects.create(
                list_name=title,
                creation_date=datetime.now(),
                tier_config=ranking_data
            )

            return redirect('detail', ranking_id=ranking.id)
    else:
        form = TierListForm()
    return render(request, 'maker.html', {'form': form})

def index(request):
    return render(request, 'home.html')

def discover(request):
    rankings = Ranking.objects.all()
    return render(request, 'discover.html', {'rankings': rankings})

def detail(request, ranking_id):
    ranking = Ranking.objects.get(id=ranking_id)
    context = {
        'ranking': ranking,
    }
    return render(request, 'detail.html', context)
