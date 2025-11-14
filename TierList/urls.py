from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('discover/', views.discover, name='discover'),
    path('maker/', views.maker, name='maker'),
    path('maker/', views.maker, name='maker'),
    path('detail/<int:ranking_id>/', views.detail, name='detail'),
]