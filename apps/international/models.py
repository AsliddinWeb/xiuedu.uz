from django.db import models


class Partner(models.Model):
    """Xalqaro hamkorlar"""
    name = models.CharField('Nomi', max_length=200)
    country = models.CharField('Davlat', max_length=100)
    logo = models.ImageField('Logo', upload_to='international/', blank=True)
    website = models.URLField('Veb sayt', blank=True)
    description = models.TextField('Tavsif', blank=True)
    agreement_date = models.DateField('Shartnoma sanasi', blank=True, null=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Xalqaro hamkor'
        verbose_name_plural = 'Xalqaro hamkorlar'
        ordering = ['order']

    def __str__(self):
        return self.name


class Grant(models.Model):
    """Grantlar"""
    title = models.CharField('Sarlavha', max_length=300)
    organization = models.CharField('Tashkilot', max_length=200)
    description = models.TextField('Tavsif')
    deadline = models.DateField('Muddat', blank=True, null=True)
    link = models.URLField('Havola', blank=True)
    is_active = models.BooleanField('Faol', default=True)
    created_at = models.DateTimeField('Yaratilgan', auto_now_add=True)

    class Meta:
        verbose_name = 'Grant'
        verbose_name_plural = 'Grantlar'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Exchange(models.Model):
    """Almashinuv dasturlari"""
    title = models.CharField('Sarlavha', max_length=300)
    country = models.CharField('Davlat', max_length=100)
    duration = models.CharField('Muddat', max_length=100, blank=True)
    description = models.TextField('Tavsif')
    requirements = models.TextField('Talablar', blank=True)
    deadline = models.DateField('Ariza muddati', blank=True, null=True)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Almashinuv dasturi'
        verbose_name_plural = 'Almashinuv dasturlari'

    def __str__(self):
        return self.title


class Agreement(models.Model):
    """Shartnomalar"""
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='agreements', verbose_name='Hamkor')
    title = models.CharField('Sarlavha', max_length=300)
    file = models.FileField('Fayl', upload_to='agreements/', blank=True)
    signed_date = models.DateField('Imzolangan sana')

    class Meta:
        verbose_name = 'Shartnoma'
        verbose_name_plural = 'Shartnomalar'
        ordering = ['-signed_date']

    def __str__(self):
        return self.title