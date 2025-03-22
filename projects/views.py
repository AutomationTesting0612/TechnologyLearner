from django.shortcuts import render, redirect, get_object_or_404

from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required(login_url='login')  # Redirects to login page if not logged in
@user_passes_test(is_admin)  # Only admin users can access
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


# def project_list(request):
#     projects = Project.objects.all()
#     return render(request, 'projects/project_list.html', {'projects': projects})

@login_required(login_url='login')
@user_passes_test(is_admin)
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})

@login_required(login_url='login')
@user_passes_test(is_admin)
def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/update_project.html', {'form': form})

@login_required(login_url='login')
@user_passes_test(is_admin)
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('project_list')