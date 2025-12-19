from django.shortcuts import render, get_object_or_404
from .models import Album, Photo, Video


def gallery(request):
    albums = Album.objects.filter(is_active=True)
    return render(request, 'gallery/gallery.html', {'albums': albums})


def album_detail(request, slug):
    album = get_object_or_404(Album, slug=slug, is_active=True)
    photos = album.photos.all()
    return render(request, 'gallery/album_detail.html', {
        'album': album,
        'photos': photos,
    })


def video_gallery(request):
    videos = Video.objects.filter(is_active=True)
    return render(request, 'gallery/video_gallery.html', {'videos': videos})