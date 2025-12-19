from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class User(AbstractUser):
    """Custom User model"""
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Xodim'),
        ('student', 'Talaba'),
    ]

    username = None
    email = models.EmailField('Email', unique=True)
    phone = models.CharField('Telefon', max_length=50, blank=True)
    role = models.CharField('Rol', max_length=20, choices=ROLE_CHOICES, default='staff')
    avatar = models.ImageField('Rasm', upload_to='avatars/', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return self.email