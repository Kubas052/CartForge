# apps/accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    # Pola podstawowe
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('phone number'), max_length=20, blank=True)
    email_verified = models.BooleanField(_('email verified'), default=False)

    # Dodatkowe pola osobowe
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    nickname = models.CharField(_('nickname'), max_length=50, blank=True, unique=True)

    # Dane dodatkowe
    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    gender = models.CharField(_('gender'), max_length=10, blank=True,
                              choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])