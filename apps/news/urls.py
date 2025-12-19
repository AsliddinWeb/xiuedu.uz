from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('announcements/', views.announcements, name='announcements'),
    path('events/', views.events, name='events'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
    path('category/<slug:slug>/', views.news_by_category, name='news_by_category'),
    path('<slug:slug>/', views.news_detail, name='news_detail'),
]