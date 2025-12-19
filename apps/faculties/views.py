from django.shortcuts import render, get_object_or_404
from .models import Faculty, Department, Teacher


def faculty_list(request):
    faculties = Faculty.objects.filter(is_active=True)
    return render(request, 'faculties/faculty_list.html', {'faculties': faculties})


def faculty_detail(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug, is_active=True)
    departments = faculty.departments.filter(is_active=True)
    return render(request, 'faculties/faculty_detail.html', {
        'faculty': faculty,
        'departments': departments,
    })


def department_list(request):
    departments = Department.objects.filter(is_active=True)
    return render(request, 'faculties/department_list.html', {'departments': departments})


def department_detail(request, slug):
    department = get_object_or_404(Department, slug=slug, is_active=True)
    teachers = department.teachers.filter(is_active=True)
    return render(request, 'faculties/department_detail.html', {
        'department': department,
        'teachers': teachers,
    })


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk, is_active=True)
    return render(request, 'faculties/teacher_detail.html', {'teacher': teacher})