from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path('bachelor/', views.bachelor_list, name='bachelor_list'),
    path('master/', views.master_list, name='master_list'),
    path('programs/<slug:slug>/', views.program_detail, name='program_detail'),
    path('schedule/', views.schedule, name='schedule'),
    path('curriculum/', views.curriculum, name='curriculum'),
]