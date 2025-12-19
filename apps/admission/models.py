from django.db import models
from apps.education.models import Program


class Admission(models.Model):
    """Qabul ma'lumotlari"""
    LEVEL_CHOICES = [
        ('bachelor', 'Bakalavriat'),
        ('master', 'Magistratura'),
    ]

    title = models.CharField('Sarlavha', max_length=200)
    level = models.CharField('Daraja', max_length=20, choices=LEVEL_CHOICES)
    content = models.TextField('Matn')
    requirements = models.TextField('Talablar', blank=True)
    documents = models.TextField('Kerakli hujjatlar', blank=True)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Qabul ma\'lumoti'
        verbose_name_plural = 'Qabul ma\'lumotlari'

    def __str__(self):
        return self.title


class Fee(models.Model):
    """To'lov narxlari"""
    FORM_CHOICES = [
        ('full_time', 'Kunduzgi'),
        ('part_time', 'Sirtqi'),
        ('evening', 'Kechki'),
    ]

    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='fees', verbose_name='Yo\'nalish')
    form = models.CharField('Ta\'lim shakli', max_length=20, choices=FORM_CHOICES)
    amount = models.DecimalField('Narx', max_digits=12, decimal_places=2)
    year = models.CharField('O\'quv yili', max_length=20)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'To\'lov narxi'
        verbose_name_plural = 'To\'lov narxlari'

    def __str__(self):
        return f"{self.program} - {self.get_form_display()}"


class Application(models.Model):
    """Online ariza"""
    STATUS_CHOICES = [
        ('new', 'Yangi'),
        ('review', 'Ko\'rib chiqilmoqda'),
        ('approved', 'Qabul qilindi'),
        ('rejected', 'Rad etildi'),
    ]

    full_name = models.CharField('F.I.O', max_length=200)
    phone = models.CharField('Telefon', max_length=50)
    email = models.EmailField('Email', blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='Yo\'nalish')
    message = models.TextField('Xabar', blank=True)
    status = models.CharField('Holat', max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField('Yuborilgan', auto_now_add=True)

    class Meta:
        verbose_name = 'Ariza'
        verbose_name_plural = 'Arizalar'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.program}"


class ExamSchedule(models.Model):
    """Imtihon jadvali"""
    title = models.CharField('Sarlavha', max_length=200)
    date = models.DateTimeField('Sana va vaqt')
    location = models.CharField('Manzil', max_length=300)
    description = models.TextField('Tavsif', blank=True)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Imtihon jadvali'
        verbose_name_plural = 'Imtihon jadvallari'
        ordering = ['date']

    def __str__(self):
        return self.title