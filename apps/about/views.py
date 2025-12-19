from django.shortcuts import render, get_object_or_404
from .models import About, Rector, Staff, Document


def about(request):
    about_info = About.objects.first()
    return render(request, 'about/about.html', {'about': about_info})


def rector(request):
    rector_info = Rector.objects.first()
    return render(request, 'about/rector.html', {'rector': rector_info})


def staff_list(request):
    staff = Staff.objects.filter(is_active=True)
    return render(request, 'about/staff_list.html', {'staff': staff})


def staff_detail(request, pk):
    person = get_object_or_404(Staff, pk=pk, is_active=True)
    return render(request, 'about/staff_detail.html', {'person': person})


def structure(request):
    return render(request, 'about/structure.html')


def history(request):
    return render(request, 'about/history.html')


def documents(request):
    docs = Document.objects.all()
    return render(request, 'about/documents.html', {'documents': docs})


def requisites(request):
    return render(request, 'about/requisites.html')