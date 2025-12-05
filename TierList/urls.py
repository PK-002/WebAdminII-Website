from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('discover/', views.discover, name='discover'),
    path('maker/', views.maker, name='maker'),
    path('new/', views.new, name='new'),
    path('config/', views.config, name='config'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('detail/<int:ranking_id>/', views.detail, name='detail'),
    path('edit/<int:ranking_id>/', views.edit, name='edit'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')
    
]