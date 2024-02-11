from rest_framework.serializers import ValidationError


class AboveZero:
    """
    Валидатор для проверки того, что цена указана выше нуля
    """
    def __init__(self, sellers_price):
        self.sellers_price = sellers_price

    def __call__(self, value):
        price = value.get(self.sellers_price)
        if price <= 0:
            raise ValidationError('Цена на товар должна быть строго выше 0.')


class SelloutPercentage:
    """
    Валидатор для проверки того, что процент распродажи меньше 100
    """
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def __call__(self, value):
        percentage = value.get(self.discount_percentage)
        if percentage >= 1:
            raise ValidationError('Скидка на товар не должна привышать 100%. Пример записи: 15% = 0.15')
