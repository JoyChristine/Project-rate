from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from .models import Project,Rate,Profile
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ('profile_pic', 'bio','location')



class projectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','context','image','url']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields= ['design','usability','content']

