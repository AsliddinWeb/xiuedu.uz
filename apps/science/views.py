from django.shortcuts import render, get_object_or_404
from .models import Project, Conference, Journal, Publication


def science(request):
    return render(request, 'science/science.html')


def projects(request):
    projects = Project.objects.filter(is_active=True)
    return render(request, 'science/projects.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, is_active=True)
    return render(request, 'science/project_detail.html', {'project': project})


def conferences(request):
    conferences = Conference.objects.filter(is_active=True)
    return render(request, 'science/conferences.html', {'conferences': conferences})


def conference_detail(request, pk):
    conference = get_object_or_404(Conference, pk=pk, is_active=True)
    return render(request, 'science/conference_detail.html', {'conference': conference})


def journals(request):
    journals = Journal.objects.filter(is_active=True)
    return render(request, 'science/journals.html', {'journals': journals})


def publications(request):
    publications = Publication.objects.all()
    return render(request, 'science/publications.html', {'publications': publications})