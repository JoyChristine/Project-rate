from email.mime import image
from unicodedata import name
from urllib.parse import DefragResult
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_pic = CloudinaryField('image',default='https://res.cloudinary.com/dz275mqsc/image/upload/v1654858776/default_nbsolf.png')
    bio = models.CharField(max_length=50)
    email =models.EmailField(max_length=20)
    location = models.CharField(max_length=20,null=True, blank=True)



    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
            instance.profile.save()


    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.user

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

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=20)
    context = models.CharField(max_length=200,blank=True)
    image = CloudinaryField('image',default='https://res.cloudinary.com/dz275mqsc/image/upload/v1654858776/default_nbsolf.png')
    date=models.DateTimeField(auto_now_add=True,null=True)
    rate=models.IntegerField(default=0)
    url=models.URLField(null=True)
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content= models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']
     
    def __str__(self):
        return self.title

    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
    
    @classmethod
    def search_project(cls, title):
        return cls.object.filter(title__icontains=title).all()
       


#  @classmethod
#     def search_profile(cls, name):
#         return cls.objects.filter(user__username__icontains=name).all()

    @classmethod
    def get_all_projects(cls):
        name=cls.object.all()
        return name



class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    design = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    usability = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    project = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}'

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()







class ProjectsAdded(models.Model):
    name = models.CharField(max_length=40)
    context = models.TextField()

class ProfilesAdded(models.Model):
    # profile_pic = models.ImageField(upload_to='profile_img/',blank=True,default='default.png')
    bio = models.TextField()
    author = models.CharField(max_length=10)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True)
    email =models.EmailField(max_length=20)
