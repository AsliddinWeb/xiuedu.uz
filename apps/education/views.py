from django.shortcuts import render, get_object_or_404
from .models import Program, Schedule, Curriculum


def bachelor_list(request):
    programs = Program.objects.filter(level='bachelor', is_active=True)
    return render(request, 'education/bachelor_list.html', {'programs': programs})


def master_list(request):
    programs = Program.objects.filter(level='master', is_active=True)
    return render(request, 'education/master_list.html', {'programs': programs})


def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug, is_active=True)
    subjects = program.subjects.all()
    curriculums = program.curriculums.all()
    return render(request, 'education/program_detail.html', {
        'program': program,
        'subjects': subjects,
        'curriculums': curriculums,
    })


def schedule(request):
    schedules = Schedule.objects.all()
    return render(request, 'education/schedule.html', {'schedules': schedules})


def curriculum(request):
    curriculums = Curriculum.objects.all()
    return render(request, 'education/curriculum.html', {'curriculums': curriculums})