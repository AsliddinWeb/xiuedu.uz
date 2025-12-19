from django.shortcuts import render, redirect
from .models import Admission, Fee, Application, ExamSchedule
from apps.education.models import Program


def admission(request):
    return render(request, 'admission/admission.html')


def bachelor(request):
    info = Admission.objects.filter(level='bachelor', is_active=True).first()
    return render(request, 'admission/bachelor.html', {'info': info})


def master(request):
    info = Admission.objects.filter(level='master', is_active=True).first()
    return render(request, 'admission/master.html', {'info': info})


def fees(request):
    fees = Fee.objects.filter(is_active=True)
    return render(request, 'admission/fees.html', {'fees': fees})


def apply(request):
    programs = Program.objects.filter(is_active=True)

    if request.method == 'POST':
        Application.objects.create(
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            program_id=request.POST.get('program'),
            message=request.POST.get('message'),
        )
        return redirect('admission:apply_success')

    return render(request, 'admission/apply.html', {'programs': programs})


def apply_success(request):
    return render(request, 'admission/apply_success.html')


def exam_schedule(request):
    exams = ExamSchedule.objects.filter(is_active=True)
    return render(request, 'admission/exam_schedule.html', {'exams': exams})