from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from .models import Project
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

ProjectFormSet = modelformset_factory(
    Project,fields = ("title","context","url")
)
