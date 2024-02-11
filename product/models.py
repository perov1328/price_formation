from django.db import models
from users.models import User
from product.constants import NULLABLE


class Product(models.Model):
    """
    Модель для Товара на маркетплейсе
    """
    salesman = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Продавец')
    title = models.CharField(max_length=50, verbose_name='Наименование товара')
    description = models.TextField(verbose_name='Описание товара')
    preview = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Фото товара')
    sellers_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена продавца')
    tax = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма налога')
    bank_commission = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Комиссия за покупку')
    seller_commission = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Комиссия за перевод продавцу')
    platform_commission = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Комиссия платформы')
    total_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Итоговая цена')
    sale = models.BooleanField(default=False, verbose_name='Распродажа')
    discount_percentage = models.FloatField(**NULLABLE, verbose_name='Процент скидки')
    price_discount = models.DecimalField(max_digits=20, decimal_places=2, **NULLABLE, verbose_name='Цена на распродаже')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return self.title

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
