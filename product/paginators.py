from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    """
    Пагинатор для вывода 10 товаров на каждой странице
    """
    page_size = 10
