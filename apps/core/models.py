from django.db import models


class SiteSettings(models.Model):
    """Sayt sozlamalari - Singleton"""
    site_name = models.CharField('Sayt nomi', max_length=200)
    logo = models.ImageField('Logo', upload_to='logo/', blank=True)
    favicon = models.ImageField('Favicon', upload_to='logo/', blank=True)

    # Aloqa
    address = models.TextField('Manzil', blank=True)
    phone = models.CharField('Telefon', max_length=50, blank=True)
    phone_2 = models.CharField('Qo\'shimcha telefon', max_length=50, blank=True)
    email = models.EmailField('Email', blank=True)

    # Ijtimoiy tarmoqlar
    telegram = models.URLField('Telegram', blank=True)
    instagram = models.URLField('Instagram', blank=True)
    facebook = models.URLField('Facebook', blank=True)
    youtube = models.URLField('YouTube', blank=True)

    # Map
    map_embed = models.TextField('Xarita (iframe)', blank=True)

    class Meta:
        verbose_name = 'Sayt sozlamasi'
        verbose_name_plural = 'Sayt sozlamalari'

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Slider(models.Model):
    """Bosh sahifa sliderlari"""
    title = models.CharField('Sarlavha', max_length=200)
    subtitle = models.CharField('Qo\'shimcha matn', max_length=300, blank=True)
    image = models.ImageField('Rasm', upload_to='sliders/')
    button_text = models.CharField('Tugma matni', max_length=50, blank=True)
    button_url = models.CharField('Tugma havolasi', max_length=200, blank=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliderlar'
        ordering = ['order']

    def __str__(self):
        return self.title


class Statistic(models.Model):
    """Raqamlarda"""
    title = models.CharField('Sarlavha', max_length=100)
    value = models.CharField('Qiymat', max_length=50)
    icon = models.CharField('Icon (class)', max_length=100, blank=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Statistika'
        verbose_name_plural = 'Statistikalar'
        ordering = ['order']

    def __str__(self):
        return self.title


class Partner(models.Model):
    """Hamkorlar"""
    name = models.CharField('Nomi', max_length=200)
    logo = models.ImageField('Logo', upload_to='partners/')
    website = models.URLField('Veb sayt', blank=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = 'Hamkor'
        verbose_name_plural = 'Hamkorlar'
        ordering = ['order']

    def __str__(self):
        return self.name