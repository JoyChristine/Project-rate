from django.contrib import admin
from django.urls import path
from . import views
from .views import ProjectList, ProjectAdd
urlpatterns = [
    # path('', views.home, name='home'),
    path('user/',views.userprofile, name='userprofile'),
    # path('api/projects/', views.ProjectList.as_view()),
    # path('api/profiles/', views.ProfileList.as_view()),
    path('addprojects/', ProjectAdd.as_view(), name='addproject'),
    path('', ProjectList.as_view(), name='project_list'),
    
]
