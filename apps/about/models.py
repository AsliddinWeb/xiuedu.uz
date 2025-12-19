from django.db import models


class About(models.Model):
    """Universitet haqida"""
    title = models.CharField('Sarlavha', max_length=200)
    content = models.TextField('Matn')
    image = models.ImageField('Rasm', upload_to='about/', blank=True)
    mission = models.TextField('Missiya', blank=True)
    vision = models.TextField('Vazifa', blank=True)

    class Meta:
        verbose_name = 'Universitet haqida'
        verbose_name_plural = 'Universitet haqida'

    def __str__(self):
        return self.title


class Rector(models.Model):
    """Rektor"""
    full_name = models.CharField('F.I.O', max_length=200)
    position = models.CharField('Lavozim', max_length=200, default='Rektor')
    photo = models.ImageField('Rasm', upload_to='staff/')
    bio = models.TextField('Biografiya')
    phone = models.CharField('Telefon', max_length=50, blank=True)
    email = models.EmailField('Email', blank=True)
    reception_days = models.CharField('Qabul kunlari', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Rektor'
        verbose_name_plural = 'Rektor'

    def __str__(self):
        return self.full_name


class Staff(models.Model):
    """Xodimlar (Rektorat)"""
    full_name = models.CharField('F.I.O', max_length=200)
    position = models.CharField('Lavozim', max_length=200)
    photo = models.ImageField('Rasm', upload_to='staff/', blank=True)
    phone = models.CharField('Telefon', max_length=50, blank=True)
    email = models.EmailField('Email', blank=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'
        ordering = ['order']

    def __str__(self):
        return self.full_name


class Document(models.Model):
    """Me'yoriy hujjatlar"""
    CATEGORY_CHOICES = [
        ('license', 'Litsenziya'),
        ('charter', 'Ustav'),
        ('regulation', 'Nizom'),
        ('order', 'Buyruq'),
        ('other', 'Boshqa'),
    ]

    title = models.CharField('Sarlavha', max_length=300)
    file = models.FileField('Fayl', upload_to='documents/')
    category = models.CharField('Kategoriya', max_length=50, choices=CATEGORY_CHOICES, default='other')
    order = models.PositiveIntegerField('Tartib', default=0)
    created_at = models.DateTimeField('Yaratilgan', auto_now_add=True)

    class Meta:
        verbose_name = 'Hujjat'
        verbose_name_plural = 'Hujjatlar'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title