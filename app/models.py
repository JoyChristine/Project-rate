from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20)
    context = models.TextField(blank=True)
    
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_img/',null=True)
    bio = models.TextField()
    author = models.CharField(max_length=10)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True)
    email =models.EmailField(max_length=20)

