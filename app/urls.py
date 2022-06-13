from django.contrib import admin
from django.urls import path
from . import views
from .views import ProjectList, ProjectAdd,MyProfileList,MyProfileList
urlpatterns = [
    # path('', views.home, name='home'),
    path('user/',views.userprofile, name='userprofile'),
    path('api/profiles/', views.MyProfileList.as_view()),
    path('api/projects/', views.MyProjectList.as_view()),
    
    path('addprojects/', ProjectAdd.as_view(), name='addproject'),
    path('', ProjectList.as_view(), name='project_list'),
    
]
