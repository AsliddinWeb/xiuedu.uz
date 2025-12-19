from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact'),
    path('success/', views.contact_success, name='contact_success'),
    path('faq/', views.faq, name='faq'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('vacancies/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('appeal/', views.appeal, name='appeal'),
    path('appeal/success/', views.appeal_success, name='appeal_success'),
]