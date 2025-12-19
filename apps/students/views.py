from django.shortcuts import render
from .models import Scholarship, Dormitory, StudentLife, StudentResource


def students(request):
    return render(request, 'students/students.html')


def scholarship(request):
    scholarships = Scholarship.objects.filter(is_active=True)
    return render(request, 'students/scholarship.html', {'scholarships': scholarships})


def dormitory(request):
    dormitories = Dormitory.objects.filter(is_active=True)
    return render(request, 'students/dormitory.html', {'dormitories': dormitories})


def library(request):
    return render(request, 'students/library.html')


def student_life(request):
    posts = StudentLife.objects.filter(is_active=True)
    return render(request, 'students/student_life.html', {'posts': posts})


def resources(request):
    resources = StudentResource.objects.all()
    return render(request, 'students/resources.html', {'resources': resources})