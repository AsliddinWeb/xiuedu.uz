from django.shortcuts import render, get_object_or_404
from .models import Category, News, Announcement, Event


def news_list(request):
    news = News.objects.filter(is_published=True)
    categories = Category.objects.all()
    return render(request, 'news/news_list.html', {
        'news': news,
        'categories': categories,
    })


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, is_published=True)
    news.views += 1
    news.save()
    return render(request, 'news/news_detail.html', {'news': news})


def news_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    news = News.objects.filter(category=category, is_published=True)
    return render(request, 'news/news_by_category.html', {
        'category': category,
        'news': news,
    })


def announcements(request):
    announcements = Announcement.objects.filter(is_active=True)
    return render(request, 'news/announcements.html', {'announcements': announcements})


def events(request):
    events = Event.objects.filter(is_active=True)
    return render(request, 'news/events.html', {'events': events})


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug, is_active=True)
    return render(request, 'news/event_detail.html', {'event': event})