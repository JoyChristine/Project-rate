
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CreateUserForm, RateForm,projectForm, UpdateUserProfileForm
from django.contrib.auth import authenticate,login,logout
from .models import Project
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProjectsAdded,ProfilesAdded,Rate,Project,Profile
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status
from django.views.generic import TemplateView,ListView
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    profile = Profile.objects.all()
    projects = Project.objects.all()

    return render(request, 'all/home.html', {"projects":projects,'profile':profile})










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
            return redirect('project_list')
        else:
            messages.info(request,'Username or password is incorrect')
    return render(request, 'accounts/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def userprofile(request,id):
    profile = Profile.objects.get(user =id)
    projects = Project.objects.all()
    # images = request.user.profile.project.all()
    if request.method == 'POST':
        updateUserProfileForm =  UpdateUserProfileForm(request.POST,request.FILES,instance=request.user.profile)

        if  updateUserProfileForm.is_valid():
             updateUserProfileForm.save()
        return HttpResponseRedirect(request.path_info)


    else:
         updateUserProfileForm =  UpdateUserProfileForm(instance=request.user.profile)
    context = {'UpdateUserProfileForm': UpdateUserProfileForm,'projects':projects, 'profile':profile, 'updateUserProfileForm': updateUserProfileForm}

    return render(request,'all/myprofile.html', context)
# def userprofile(request,id):
#     profile = Profile.objects.get(user =id)
#     return render(request, 'all/myprofile.html',{"profile":profile})

# def userprofile(request,id):
#     profile = get_object_or_404(User, username = id)
#     if request.user == profile:
#         return redirect('userprofile',username =request.user.username)
#     user_projects = profile.profile.projects.all()

#     context = {
#         'profile':profile,
#         'user_projects':user_projects,

#     }

#     return render(request,'all/myprofile.html', context)

    
# details when u click on a project
# class ProjectDetails(DetailView):
#     model = Project
#     projects = Project.objects.all()
#     template_name = 'all/project_detail.html'
#     context_object_name = 'project'
   


def ProjectDetails(request,id):
    try:
        project = Project.objects.get(id=id)
        all = Rate.objects.filter(project=id)
        # print(all)
    except Exception as error:
        raise Http404()

    total = 0
    for i in all:
        total+=i.design
        total+=i.content
        total+=i.usability

    if total > 0:
        average = round(total/3,1)
    else:
        average =0

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = id
            rate.save()

        return redirect('project_details',id)
    else:
        form = RateForm()
    
    rates = Rate.objects.filter(project=id)
    design=[]
    usability = []
    content =[]

    for rate in rates:
        design.append(rate.design)
        usability.append(rate.usability)
        content.append(rate.content)

    if len(usability) > 0 and len(usability) <=10 or len(content) > 0 and len(content) <=10 or len(design) > 0 and len(design) <= 10:
        usability_average = round(sum(usability)/len(usability),1)
        design_average = round(sum(design)/len(design),1)
        content_average = round(sum(content)/len(content),1)

        total_average = round((usability_average+design_average+content_average)/3,1)

    else:
        usability_average = 0
        design_average = 0
        content_average = 0
        total_average = 0


    ratearray = []
    for i in rates:
        ratearray.append(i.user_id)

    alreadyrated =ratearray

    context = {
        'form': form,
        'project': project,
        'usability':usability_average,
        'design':design_average,
        'content':content_average,
        'total_average':total_average,
        'average':average,
        'alreadyrated':alreadyrated,
        'all':all,


    }
    return render(request, 'all/project_detail.html',context)
    

def addProject(request):
    current_user = request.user
    # user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES)
        if form.is_valid:
            new_project = form.save(commit = False)
            new_project.user = current_user
            new_project.save()
        return redirect('home')  
    else:
        form = projectForm()
    return render(request,'all/addproject.html',{'form':form})    








# view all projects
class ProjectList(ListView):
    model = Project
    project = Project.objects.order_by('date')
    context_object_name = 'project'
    template_name = 'all/home.html'

    
@login_required(login_url='login')
def projectSearch(request):
    if request.method == 'POST':
        searched = request.POST['searched']

        project_results = Project.objects.filter(title__contains=searched)

        return render(request, 'all/results.html', {'searched':searched,"project_results":project_results})
    else:
        
        return render(request, 'all/results.html')




# def projectSearch(request):
#     if 'search_p' in request.GET and request.GET['search_p']:
#         title = request.GET.get("search_p")
#         results = Project.search_project(title)
#         print(results)
#         message = f'name'
#         context = {
#             "results": results,
#             "message": message 
#         }
#         return render(request, 'all/results.html', context)
#     else:
#         message = "Try again"
#     return render(request, 'all/results.html', {'message': message})

    



# class ProjectAdd(TemplateView):
#     template_name = 'all/addproject.html'

#     # func to handle get request
#     def get(self, *args, **kwargs):
#         formset =  ProjectFormSet(queryset=Project.objects.none())
#         return self.render_to_response({'project_formset':formset})

#     # func to handle POST request
#     def post(self, *args, **kwargs):
#         formset = ProjectFormSet(data=self.request.POST)

#         if formset.is_valid():
#             formset.save()
#             return redirect(reverse_lazy("project_list"))

#         return self.render_to_response({'project_formset':formset})



















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