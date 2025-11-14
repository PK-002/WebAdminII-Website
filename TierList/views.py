from django.shortcuts import render

# Create your views here.

from django.contrib import admin
from .models import Ranking

admin.site.register(Ranking)