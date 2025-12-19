from django.db import models


class Category(models.Model):
    """Kategoriyalar"""
    name = models.CharField('Nomi', max_length=100)
    slug = models.SlugField('Slug', max_length=100, unique=True)
    order = models.PositiveIntegerField('Tartib', default=0)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        ordering = ['order']

    def __str__(self):
        return self.name


class News(models.Model):
    """Yangiliklar"""
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='news', verbose_name='Kategoriya')
    title = models.CharField('Sarlavha', max_length=300)
    slug = models.SlugField('Slug', max_length=300, unique=True)
    content = models.TextField('Matn')
    image = models.ImageField('Rasm', upload_to='news/')
    views = models.PositiveIntegerField('Ko\'rishlar', default=0)
    is_published = models.BooleanField('Nashr qilingan', default=True)
    created_at = models.DateTimeField('Yaratilgan', auto_now_add=True)
    updated_at = models.DateTimeField('Yangilangan', auto_now=True)

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Announcement(models.Model):
    """E'lonlar"""
    title = models.CharField('Sarlavha', max_length=300)
    content = models.TextField('Matn')
    start_date = models.DateField('Boshlanish', blank=True, null=True)
    end_date = models.DateField('Tugash', blank=True, null=True)
    is_active = models.BooleanField('Faol', default=True)
    created_at = models.DateTimeField('Yaratilgan', auto_now_add=True)

    class Meta:
        verbose_name = 'E\'lon'
        verbose_name_plural = 'E\'lonlar'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Event(models.Model):
    """Tadbirlar"""
    title = models.CharField('Sarlavha', max_length=300)
    slug = models.SlugField('Slug', max_length=300, unique=True)
    description = models.TextField('Tavsif')
    image = models.ImageField('Rasm', upload_to='events/', blank=True)
    date = models.DateTimeField('Sana va vaqt')
    location = models.CharField('Manzil', max_length=300)
    is_active = models.BooleanField('Faol', default=True)
    created_at = models.DateTimeField('Yaratilgan', auto_now_add=True)

    class Meta:
        verbose_name = 'Tadbir'
        verbose_name_plural = 'Tadbirlar'
        ordering = ['-date']

    def __str__(self):
        return self.title