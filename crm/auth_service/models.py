from django.contrib import admin
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    second_name = models.CharField(max_length=100, default='', verbose_name='Отчество')
    phone_number = models.CharField(max_length=20, default='', verbose_name='Номер телефона')

    fiz_tin = models.CharField(max_length=12, default='', verbose_name='ИНН')

    profile_image = models.ImageField(
        upload_to=settings.MEDIA_ROOT,
        null=True,
        blank=True,
        verbose_name='Фото профиля'
        )

    is_shop_owner = models.BooleanField(default=False, verbose_name='Владелец магазина')
    is_supplier = models.BooleanField(default=False, verbose_name='Поставщик')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.second_name}'

    @admin.display(description='ФИО')
    def get_full_name(self) -> str:
        return f'{super().get_full_name()} {self.second_name}'