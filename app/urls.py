from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views
from .views import MyProfileList,ProjectList,addProject
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', views.home, name='home'),
    path('user/<id>/',views.userprofile, name='profile'),
    path('api/profiles/', views.MyProfileList.as_view()),
    path('api/projects/', views.MyProjectList.as_view()),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutuser, name='logout'),
    path('', views.signin, name='login'),
    path('addprojects/', views.addProject, name='project'),
    path('home', ProjectList.as_view(), name='project_list'),
    path('project/<int:id>/',views.ProjectDetails,name='project_details'),
    path('search/', views.projectSearch, name='search'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)