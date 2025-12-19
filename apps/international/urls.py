from django.urls import path
from . import views

app_name = 'international'

urlpatterns = [
    path('', views.international, name='international'),
    path('partners/', views.partners, name='partners'),
    path('grants/', views.grants, name='grants'),
    path('grants/<int:pk>/', views.grant_detail, name='grant_detail'),
    path('exchange/', views.exchange, name='exchange'),
    path('exchange/<int:pk>/', views.exchange_detail, name='exchange_detail'),
]