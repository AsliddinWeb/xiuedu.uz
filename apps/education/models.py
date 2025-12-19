from django.db import models
from apps.faculties.models import Faculty


class Program(models.Model):
    """Ta'lim yo'nalishlari"""
    LEVEL_CHOICES = [
        ('bachelor', 'Bakalavriat'),
        ('master', 'Magistratura'),
    ]

    FORM_CHOICES = [
        ('full_time', 'Kunduzgi'),
        ('part_time', 'Sirtqi'),
        ('evening', 'Kechki'),
    ]

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='programs', verbose_name='Fakultet')
    name = models.CharField('Nomi', max_length=200)
    slug = models.SlugField('Slug', max_length=200, unique=True)
    code = models.CharField('Kod', max_length=50, blank=True)
    level = models.CharField('Daraja', max_length=20, choices=LEVEL_CHOICES)
    form = models.CharField('Ta\'lim shakli', max_length=20, choices=FORM_CHOICES, default='full_time')
    duration = models.CharField('O\'qish muddati', max_length=50, blank=True)
    description = models.TextField('Tavsif', blank=True)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Ta\'lim yo\'nalishi'
        verbose_name_plural = 'Ta\'lim yo\'nalishlari'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"


class Subject(models.Model):
    """Fanlar"""
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='subjects', verbose_name='Yo\'nalish')
    name = models.CharField('Fan nomi', max_length=200)
    code = models.CharField('Kod', max_length=50, blank=True)
    credits = models.PositiveIntegerField('Kredit', default=0)
    semester = models.PositiveIntegerField('Semestr', default=1)

    class Meta:
        verbose_name = 'Fan'
        verbose_name_plural = 'Fanlar'
        ordering = ['semester', 'name']

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """Dars jadvali"""
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='schedules', verbose_name='Fakultet')
    title = models.CharField('Sarlavha', max_length=200)
    file = models.FileField('Fayl', upload_to='schedules/')
    updated_at = models.DateTimeField('Yangilangan', auto_now=True)

    class Meta:
        verbose_name = 'Dars jadvali'
        verbose_name_plural = 'Dars jadvallari'

    def __str__(self):
        return self.title


class Curriculum(models.Model):
    """O'quv reja"""
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='curriculums',
                                verbose_name='Yo\'nalish')
    year = models.CharField('O\'quv yili', max_length=20)
    file = models.FileField('Fayl', upload_to='curriculums/')

    class Meta:
        verbose_name = 'O\'quv reja'
        verbose_name_plural = 'O\'quv rejalar'

    def __str__(self):
        return f"{self.program} - {self.year}"