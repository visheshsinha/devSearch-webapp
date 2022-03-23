from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.test import tag
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    tags = projectObject.tag.all()
    reviews = projectObject.review_set.all()
    context = {"project": projectObject, "tags": tags, "reviews": reviews}
    return render(request, "projects/single_projects.html", context)

def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        # print(request.POST)
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('projects')


    context = {'form': form}
    return render(request, "projects/project_form.html", context)