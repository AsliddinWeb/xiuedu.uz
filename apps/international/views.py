from django.shortcuts import render, get_object_or_404
from .models import Partner, Grant, Exchange, Agreement


def international(request):
    return render(request, 'international/international.html')


def partners(request):
    partners = Partner.objects.filter(is_active=True)
    return render(request, 'international/partners.html', {'partners': partners})


def grants(request):
    grants = Grant.objects.filter(is_active=True)
    return render(request, 'international/grants.html', {'grants': grants})


def grant_detail(request, pk):
    grant = get_object_or_404(Grant, pk=pk, is_active=True)
    return render(request, 'international/grant_detail.html', {'grant': grant})


def exchange(request):
    programs = Exchange.objects.filter(is_active=True)
    return render(request, 'international/exchange.html', {'programs': programs})


def exchange_detail(request, pk):
    program = get_object_or_404(Exchange, pk=pk, is_active=True)
    return render(request, 'international/exchange_detail.html', {'program': program})