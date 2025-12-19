from django.db import models


class Faculty(models.Model):
    """Fakultetlar"""
    name = models.CharField('Nomi', max_length=200)
    slug = models.SlugField('Slug', max_length=200, unique=True)
    dean = models.CharField('Dekan', max_length=200, blank=True)
    description = models.TextField('Tavsif', blank=True)
    image = models.ImageField('Rasm', upload_to='faculties/', blank=True)
    phone = models.CharField('Telefon', max_length=50, blank=True)
    email = models.EmailField('Email', blank=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Fakultet'
        verbose_name_plural = 'Fakultetlar'
        ordering = ['order']

    def __str__(self):
        return self.name


class Department(models.Model):
    """Kafedralar"""
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='departments', verbose_name='Fakultet')
    name = models.CharField('Nomi', max_length=200)
    slug = models.SlugField('Slug', max_length=200, unique=True)
    head = models.CharField('Kafedra mudiri', max_length=200, blank=True)
    description = models.TextField('Tavsif', blank=True)
    phone = models.CharField('Telefon', max_length=50, blank=True)
    email = models.EmailField('Email', blank=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Kafedra'
        verbose_name_plural = 'Kafedralar'
        ordering = ['order']

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """O'qituvchilar"""
    DEGREE_CHOICES = [
        ('professor', 'Professor'),
        ('dotsent', 'Dotsent'),
        ('phd', 'PhD'),
        ('teacher', 'O\'qituvchi'),
        ('assistant', 'Assistent'),
    ]

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers', verbose_name='Kafedra')
    full_name = models.CharField('F.I.O', max_length=200)
    position = models.CharField('Lavozim', max_length=200)
    degree = models.CharField('Ilmiy daraja', max_length=50, choices=DEGREE_CHOICES, blank=True)
    photo = models.ImageField('Rasm', upload_to='teachers/', blank=True)
    bio = models.TextField('Biografiya', blank=True)
    phone = models.CharField('Telefon', max_length=50, blank=True)
    email = models.EmailField('Email', blank=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'O\'qituvchi'
        verbose_name_plural = 'O\'qituvchilar'
        ordering = ['order']

    def __str__(self):
        return self.full_name