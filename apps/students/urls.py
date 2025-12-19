from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.students, name='students'),
    path('scholarship/', views.scholarship, name='scholarship'),
    path('dormitory/', views.dormitory, name='dormitory'),
    path('library/', views.library, name='library'),
    path('life/', views.student_life, name='student_life'),
    path('resources/', views.resources, name='resources'),
]