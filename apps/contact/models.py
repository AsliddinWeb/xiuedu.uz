from django.db import models


class Contact(models.Model):
    """Murojaat formasi"""
    full_name = models.CharField('F.I.O', max_length=200)
    phone = models.CharField('Telefon', max_length=50)
    email = models.EmailField('Email', blank=True)
    subject = models.CharField('Mavzu', max_length=200)
    message = models.TextField('Xabar')
    is_read = models.BooleanField('O\'qilgan', default=False)
    created_at = models.DateTimeField('Yuborilgan', auto_now_add=True)

    class Meta:
        verbose_name = 'Murojaat'
        verbose_name_plural = 'Murojaatlar'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.subject}"


class FAQ(models.Model):
    """Ko'p so'raladigan savollar"""
    question = models.CharField('Savol', max_length=300)
    answer = models.TextField('Javob')
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Savol-javob'
        verbose_name_plural = 'Savol-javoblar'
        ordering = ['order']

    def __str__(self):
        return self.question


class Vacancy(models.Model):
    """Vakansiyalar"""
    title = models.CharField('Lavozim', max_length=200)
    department = models.CharField('Bo\'lim', max_length=200, blank=True)
    description = models.TextField('Tavsif')
    requirements = models.TextField('Talablar')
    salary = models.CharField('Maosh', max_length=100, blank=True)
    deadline = models.DateField('Muddat', blank=True, null=True)
    is_active = models.BooleanField('Faol', default=True)
    created_at = models.DateTimeField('Yaratilgan', auto_now_add=True)

    class Meta:
        verbose_name = 'Vakansiya'
        verbose_name_plural = 'Vakansiyalar'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Appeal(models.Model):
    """Rektorga murojaat"""
    STATUS_CHOICES = [
        ('new', 'Yangi'),
        ('review', 'Ko\'rib chiqilmoqda'),
        ('answered', 'Javob berildi'),
        ('closed', 'Yopildi'),
    ]

    full_name = models.CharField('F.I.O', max_length=200)
    phone = models.CharField('Telefon', max_length=50)
    email = models.EmailField('Email', blank=True)
    subject = models.CharField('Mavzu', max_length=200)
    message = models.TextField('Xabar')
    status = models.CharField('Holat', max_length=20, choices=STATUS_CHOICES, default='new')
    answer = models.TextField('Javob', blank=True)
    created_at = models.DateTimeField('Yuborilgan', auto_now_add=True)

    class Meta:
        verbose_name = 'Rektorga murojaat'
        verbose_name_plural = 'Rektorga murojaatlar'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.subject}"