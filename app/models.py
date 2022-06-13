from email.mime import image
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=20)
    context = models.TextField(max_length=120,blank=True)
    image=models.ImageField(upload_to='project_img',null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    rate=models.IntegerField(default=0)
    url=models.URLField(null=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
    
    @classmethod
    def search_by_name(cls, search_term):
        name = cls.object.filter(project__icontains=search_term)
        return name

    @classmethod
    def get_all_projects(cls):
        name=cls.object.all()
        return name


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_img/',null=True)
    bio = models.TextField()
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True)
    email =models.EmailField(max_length=20)

    def __str__(self):
        return f'{self.author}'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def search_by_name(cls, search_term):
        author = cls.object.filter(profile__icontains=search_term)
        return author

    @classmethod
    def get_all_profiles(cls):
        author=cls.object.all()
        return author

class ProjectsAdded(models.Model):
    name = models.CharField(max_length=40)
    context = models.TextField()

class ProfilesAdded(models.Model):
    profile_pic = models.ImageField(upload_to='profile_img/',null=True)
    bio = models.TextField()
    author = models.CharField(max_length=10)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True)
    email =models.EmailField(max_length=20)
