from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from ..common.models import CreatedUpdatedDeleted
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, CreatedUpdatedDeleted):

    class Gender(models.TextChoices):
        M = ('M', 'Male')
        F = ('F', 'Female')


    def upload_to(instance, filename):
        return f'{instance.email}/{filename}'


    first_name = models.CharField('First name', max_length=40)
    middle_name = models.CharField('Middle name', max_length=40)
    last_name = models.CharField('Last name', max_length=40)

    email = models.EmailField('Email', max_length=100, unique=True)

    gender = models.CharField('Gender', max_length=1, choices=Gender.choices)
    avatar = models.ImageField('Avatar', upload_to=upload_to, blank=True, null=True)

    country = models.CharField('Country', max_length=40, blank=True, null=True)
    phone_number = models.CharField('Phone number', max_length=40, blank=True, null=True)
    telegram_username = models.CharField('Telegram username', max_length=40, blank=True, null=True)

    is_staff = models.BooleanField('Is staff', default=False)
    is_active = models.BooleanField('Is active', default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email