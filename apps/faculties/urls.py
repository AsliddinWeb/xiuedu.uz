from django.urls import path
from . import views

app_name = 'faculties'

urlpatterns = [
    path('', views.faculty_list, name='faculty_list'),
    path('<slug:slug>/', views.faculty_detail, name='faculty_detail'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/<slug:slug>/', views.department_detail, name='department_detail'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
]