from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, FAQ, Vacancy, Appeal


def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        return redirect('contact:contact_success')

    return render(request, 'contact/contact.html')


def contact_success(request):
    return render(request, 'contact/contact_success.html')


def faq(request):
    faqs = FAQ.objects.filter(is_active=True)
    return render(request, 'contact/faq.html', {'faqs': faqs})


def vacancies(request):
    vacancies = Vacancy.objects.filter(is_active=True)
    return render(request, 'contact/vacancies.html', {'vacancies': vacancies})


def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk, is_active=True)
    return render(request, 'contact/vacancy_detail.html', {'vacancy': vacancy})


def appeal(request):
    if request.method == 'POST':
        Appeal.objects.create(
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        return redirect('contact:appeal_success')

    return render(request, 'contact/appeal.html')


def appeal_success(request):
    return render(request, 'contact/appeal_success.html')