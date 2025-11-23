from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('discover/', views.discover, name='discover'),
    path('maker/', views.maker, name='maker'),
    path('new/', views.new, name='new'),
    path('config/', views.config, name='config'),
    path('detail/<int:ranking_id>/', views.detail, name='detail'),
    path('create/<int:ranking_id>/', views.create, name='create'),
]