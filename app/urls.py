from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profiles/', views.ProfileList.as_view()),
    
]
