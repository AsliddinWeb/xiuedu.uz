from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('videos/', views.video_gallery, name='video_gallery'),
    path('<slug:slug>/', views.album_detail, name='album_detail'),
]