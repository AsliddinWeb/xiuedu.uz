from django.shortcuts import render, get_object_or_404
from .models import Slider, Statistic, Partner, SiteSettings


def home(request):
    context = {
        'sliders': Slider.objects.filter(is_active=True),
        'statistics': Statistic.objects.filter(is_active=True),
        'partners': Partner.objects.filter(is_active=True),
    }
    return render(request, 'core/home.html', context)


def search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        from apps.news.models import News
        results = News.objects.filter(
            title__icontains=query,
            is_published=True
        )

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'core/search.html', context)