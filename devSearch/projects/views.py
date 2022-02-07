from django.shortcuts import render
from django.http import HttpResponse
from django.test import tag
from .models import Project


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
