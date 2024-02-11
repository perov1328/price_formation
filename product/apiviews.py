from rest_framework.permissions import IsAdminUser, IsAuthenticated
from product.models import Product
from product.permissions import IsSalesman, IsModerator, IsSalesmanUpdate
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from product.paginators import ProductPagination
from product.serializers import ProductListSerializer, ProductCreateSerializer, ProductUpdateSerializer
from product.services import price_formation, price_formated_for_sale


class ProductCreateAPIView(CreateAPIView):
    """
    Контроллер для создания сущностей модели Товара
    """
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated, IsSalesman]

    def perform_create(self, serializer):
        price_formation(self, serializer)


class ProductListAPIView(ListAPIView):
    """
    Контроллер для просмотра списка всех сущностей модели Товаров
    """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = ProductPagination


class ProductRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотра конкретной сущности модели Товаров
    """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductUpdateAPIView(UpdateAPIView):
    """
    Контроллер для обновления сущностей модели Товара
    """
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsSalesmanUpdate]

    def perform_update(self, serializer):
        price_formated_for_sale(self, serializer)


class ProductDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаление сущностей модели Товара
    """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [IsSalesman | IsModerator, IsAdminUser]
