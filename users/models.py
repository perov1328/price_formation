from django.db import models
from django.contrib.auth.models import AbstractUser
from users.constants import USER_STATUS, NULLABLE


class User(AbstractUser):
    """
    Модель для пользователя
    """
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    status = models.CharField(max_length=10, choices=USER_STATUS, default='User', verbose_name='Роль пользователя')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'{self.email} - {self.first_name} {self.last_name} ({self.status})'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
