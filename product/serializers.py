from rest_framework.serializers import ModelSerializer
from product.models import Product
from rest_framework import serializers
from product.validators import AboveZero, SelloutPercentage


class ProductCreateSerializer(ModelSerializer):
    """
    Сериализатор для работы с моделью Товара
    """
    tax = serializers.FloatField(read_only=True)
    bank_commission = serializers.FloatField(read_only=True)
    seller_commission = serializers.FloatField(read_only=True)
    platform_commission = serializers.FloatField(read_only=True)
    total_price = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'sellers_price', 'preview', 'tax',
                  'bank_commission', 'seller_commission', 'platform_commission', 'total_price', ]
        validators = [
            AboveZero(sellers_price='sellers_price')
        ]


class ProductListSerializer(ModelSerializer):
    """
    Сериализатор для вывода списка всех Товаров
    """
    class Meta:
        model = Product
        fields = ('id', 'salesman', 'title', 'description',
                  'total_price', 'sale', 'discount_percentage', 'price_discount',)


class ProductUpdateSerializer(ModelSerializer):
    """
    Сериализатор для обновления модели Товара
    """
    price_discount = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'sellers_price', 'total_price',
                  "sale", 'discount_percentage', 'price_discount',)
        read_only_fields = ('total_price',)
        validators = [
            AboveZero(sellers_price='sellers_price'),
            SelloutPercentage(discount_percentage='discount_percentage')
        ]
