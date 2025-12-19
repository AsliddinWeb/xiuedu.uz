from django.db import models


class Scholarship(models.Model):
    """Stipendiyalar"""
    title = models.CharField('Sarlavha', max_length=200)
    description = models.TextField('Tavsif')
    amount = models.CharField('Miqdor', max_length=100, blank=True)
    requirements = models.TextField('Talablar', blank=True)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Stipendiya'
        verbose_name_plural = 'Stipendiyalar'

    def __str__(self):
        return self.title


class Dormitory(models.Model):
    """Yotoqxona"""
    name = models.CharField('Nomi', max_length=200)
    address = models.CharField('Manzil', max_length=300)
    capacity = models.PositiveIntegerField('Sig\'imi', default=0)
    description = models.TextField('Tavsif', blank=True)
    image = models.ImageField('Rasm', upload_to='dormitory/', blank=True)
    phone = models.CharField('Telefon', max_length=50, blank=True)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Yotoqxona'
        verbose_name_plural = 'Yotoqxonalar'

    def __str__(self):
        return self.name


class StudentLife(models.Model):
    """Talabalar hayoti"""
    title = models.CharField('Sarlavha', max_length=200)
    content = models.TextField('Matn')
    image = models.ImageField('Rasm', upload_to='student_life/', blank=True)
    date = models.DateField('Sana', blank=True, null=True)
    is_active = models.BooleanField('Faol', default=True)
    created_at = models.DateTimeField('Yaratilgan', auto_now_add=True)

    class Meta:
        verbose_name = 'Talabalar hayoti'
        verbose_name_plural = 'Talabalar hayoti'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class StudentResource(models.Model):
    """Talabalar uchun resurslar"""
    CATEGORY_CHOICES = [
        ('guide', 'Qo\'llanma'),
        ('form', 'Shakl/Blanка'),
        ('other', 'Boshqa'),
    ]

    title = models.CharField('Sarlavha', max_length=200)
    file = models.FileField('Fayl', upload_to='student_resources/')
    category = models.CharField('Kategoriya', max_length=50, choices=CATEGORY_CHOICES, default='other')
    order = models.PositiveIntegerField('Tartib', default=0)

    class Meta:
        verbose_name = 'Resurs'
        verbose_name_plural = 'Resurslar'
        ordering = ['order']

    def __str__(self):
        return self.title