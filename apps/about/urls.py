from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about, name='about'),
    path('rector/', views.rector, name='rector'),
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<int:pk>/', views.staff_detail, name='staff_detail'),
    path('structure/', views.structure, name='structure'),
    path('history/', views.history, name='history'),
    path('documents/', views.documents, name='documents'),
    path('requisites/', views.requisites, name='requisites'),
]