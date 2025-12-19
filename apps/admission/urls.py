from django.urls import path
from . import views

app_name = 'admission'

urlpatterns = [
    path('', views.admission, name='admission'),
    path('bachelor/', views.bachelor, name='bachelor'),
    path('master/', views.master, name='master'),
    path('fees/', views.fees, name='fees'),
    path('apply/', views.apply, name='apply'),
    path('apply/success/', views.apply_success, name='apply_success'),
    path('exams/', views.exam_schedule, name='exam_schedule'),
]