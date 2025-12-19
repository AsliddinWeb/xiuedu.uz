from django.db import models


class Album(models.Model):
    """Foto albomlar"""
    title = models.CharField('Sarlavha', max_length=200)
    slug = models.SlugField('Slug', max_length=200, unique=True)
    cover = models.ImageField('Muqova', upload_to='gallery/covers/')
    description = models.TextField('Tavsif', blank=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)
    created_at = models.DateTimeField('Yaratilgan', auto_now_add=True)

    class Meta:
        verbose_name = 'Albom'
        verbose_name_plural = 'Albomlar'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Photo(models.Model):
    """Rasmlar"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos', verbose_name='Albom')
    image = models.ImageField('Rasm', upload_to='gallery/photos/')
    caption = models.CharField('Izoh', max_length=200, blank=True)
    order = models.PositiveIntegerField('Tartib', default=0)

    class Meta:
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasmlar'
        ordering = ['order']

    def __str__(self):
        return self.caption or f"Rasm {self.pk}"


class Video(models.Model):
    """YouTube videolar"""
    title = models.CharField('Sarlavha', max_length=200)
    youtube_url = models.URLField('YouTube havola')
    description = models.TextField('Tavsif', blank=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)
    created_at = models.DateTimeField('Yaratilgan', auto_now_add=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videolar'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    @property
    def youtube_id(self):
        """YouTube video ID ni ajratib olish"""
        url = self.youtube_url
        if 'youtu.be/' in url:
            return url.split('youtu.be/')[-1].split('?')[0]
        if 'watch?v=' in url:
            return url.split('watch?v=')[-1].split('&')[0]
        if 'embed/' in url:
            return url.split('embed/')[-1].split('?')[0]
        return url

    @property
    def embed_url(self):
        """Embed URL"""
        return f"https://www.youtube.com/embed/{self.youtube_id}"

    @property
    def thumbnail(self):
        """YouTube thumbnail"""
        return f"https://img.youtube.com/vi/{self.youtube_id}/hqdefault.jpg"