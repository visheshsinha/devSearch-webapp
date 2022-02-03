from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website',
        'top_rated': True
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work',
        'top_rated': False
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community',
        'top_rated': True
    }
]


def projects(request):
    context = {"projects":projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObject = None
    for project in projectsList:
        if pk == project["id"]:
            projectObject = project

    return render(request, 'projects/single_projects.html', {"project":projectObject})