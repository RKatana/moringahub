from django.shortcuts import render,redirect
from .models import Student,Projects,Comments,Ideas
from .forms import(
    ProfileForm,
    CommentForm,
    ProjectForm,
    IdeaForm
)

# Create your views here.
def home(request):
    projects=Projects.objects.all()
    return render(request,'index.html',{'projects':projects})

def profile(request):
    ideas=Ideas.objects.filter(student_id=request.user.id)
    profile =Student.objects.get(name_id=request.user.id)
    return render(request,'profile.html',{'profile':profile,'ideas':ideas})

def update_profile(request):
    student =Student.objects.get(name_id=request.user.id)
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=student)
    return render(request,'edit_profile.html',{'form':form,'student':student})

def projects(request):
    projects=Projects.objects.all()
    return render(request,'projects.html',{'projects':projects})

def draft_idea(request):
    study =Student.objects.get(name_id=request.user.id)
    if request.method=='POST':
        student=Ideas(student=study)
        form =IdeaForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            redirect('profile')
    else:
        form =IdeaForm()
    return render(request,'drafts.html',{'form':form})

def post_projects(request):
    user =request.user
    study=Student.objects.get(name_id=user.id)
    if request.method=='POST':
        student=Projects(student=study)
        form =ProjectForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request,'post_project.html',{'form':form})


def search_projects(request):
    if "projects" in request.GET and request.GET["projects"]:
        s_class = request.GET.get("projects")
        projects = Projects.search_by_class(s_class)
        return render(request, "results.html", {"projects":projects,})


def sign_out(request):
    return render(request,'registration/logout.html')