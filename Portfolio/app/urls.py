from django.urls import path
from django.contrib.auth import views as auth_views
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('robux/', views.robux, name='robux'),
]