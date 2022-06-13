
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CreateUserForm, ProjectFormSet
from django.contrib.auth import authenticate,login,logout
from .models import Project
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProjectsAdded,ProfilesAdded
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status
from django.views.generic import TemplateView,ListView
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    project = Project.objects.all()
    users = User.objects.all()


    return render(request, 'all/home.html',{'project': project, 'users': users})

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')



    context = {'form':form}
    return render(request, 'accounts/register.html',context)

def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect')

    return render(request, 'accounts/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def userprofile(request,username):
    user_prof = get_object_or_404(User, username = username)
    if request.user == user_prof:
        return redirect('userprofile',username =request.user.username)
    user_projects = user_prof.profile.projects.all()

    # followers = Follow.objects.flter(followed=user_prof.profile)
    # follow_status = None

    # for follower in followers:
    #     if request.user.profile ==follower.follower:
    #         follow_status = True
    #     else:
    #         follow_status = false

    context = {
        'user_prof':user_prof,
        'user_projects':user_projects,

    }

    return render(request,'all/myprofile.html', context)

    
class ProjectList(ListView):
    model = Project
    template_name = 'all/home.html'



class ProjectAdd(TemplateView):
    template_name = 'all/addproject.html'

    # func to handle get request
    def get(self, *args, **kwargs):
        formset =  ProjectFormSet(queryset=Project.objects.none())
        return self.render_to_response({'project_formset':formset})

    # func to handle POST request
    def post(self, *args, **kwargs):
        formset = ProjectFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("project_list"))

        return self.render_to_response({'project_formset':formset})



















# api's
class MyProjectList(APIView):
    def get(self, request, format=None):
        all_projects = ProjectsAdded.objects.all()
        serializers = ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class MyProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = ProfilesAdded.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)