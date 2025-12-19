from django.db import models


class Project(models.Model):
    """Ilmiy loyihalar"""
    STATUS_CHOICES = [
        ('active', 'Faol'),
        ('completed', 'Yakunlangan'),
        ('planned', 'Rejalashtirilgan'),
    ]

    title = models.CharField('Sarlavha', max_length=300)
    description = models.TextField('Tavsif')
    leader = models.CharField('Rahbar', max_length=200, blank=True)
    start_date = models.DateField('Boshlanish', blank=True, null=True)
    end_date = models.DateField('Tugash', blank=True, null=True)
    status = models.CharField('Holat', max_length=20, choices=STATUS_CHOICES, default='active')
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Ilmiy loyiha'
        verbose_name_plural = 'Ilmiy loyihalar'

    def __str__(self):
        return self.title


class Conference(models.Model):
    """Konferensiyalar"""
    title = models.CharField('Sarlavha', max_length=300)
    date = models.DateField('Sana')
    location = models.CharField('Manzil', max_length=300)
    description = models.TextField('Tavsif', blank=True)
    image = models.ImageField('Rasm', upload_to='conferences/', blank=True)
    file = models.FileField('Fayl', upload_to='conferences/', blank=True)
    is_upcoming = models.BooleanField('Kutilayotgan', default=True)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Konferensiya'
        verbose_name_plural = 'Konferensiyalar'
        ordering = ['-date']

    def __str__(self):
        return self.title


class Journal(models.Model):
    """Ilmiy jurnallar"""
    name = models.CharField('Nomi', max_length=200)
    issn = models.CharField('ISSN', max_length=50, blank=True)
    description = models.TextField('Tavsif', blank=True)
    cover = models.ImageField('Muqova', upload_to='journals/', blank=True)
    website = models.URLField('Veb sayt', blank=True)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Jurnal'
        verbose_name_plural = 'Jurnallar'

    def __str__(self):
        return self.name


class Publication(models.Model):
    """Ilmiy nashrlar"""
    title = models.CharField('Sarlavha', max_length=300)
    authors = models.CharField('Mualliflar', max_length=500)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='publications', verbose_name='Jurnal', blank=True, null=True)
    year = models.PositiveIntegerField('Yil')
    doi = models.CharField('DOI', max_length=200, blank=True)
    link = models.URLField('Havola', blank=True)

    class Meta:
        verbose_name = 'Nashr'
        verbose_name_plural = 'Nashrlar'
        ordering = ['-year']

    def __str__(self):
        return self.title