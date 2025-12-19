from django.urls import path
from . import views

app_name = 'science'

urlpatterns = [
    path('', views.science, name='science'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('conferences/', views.conferences, name='conferences'),
    path('conferences/<int:pk>/', views.conference_detail, name='conference_detail'),
    path('journals/', views.journals, name='journals'),
    path('publications/', views.publications, name='publications'),
]