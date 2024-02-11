from rest_framework.permissions import BasePermission


class IsSalesman(BasePermission):
    """
    Кастомные права доступа для определения продавца товара
    """
    message = "Вы не являетесь продавцом."

    def has_permission(self, request, view):
        return request.user.status == 'Salesman'


class IsModerator(BasePermission):
    """
    Кастомные права доступа для определения модератора
    """
    message = "Вы не являетесь модератором."

    def has_object_permission(self, request, view, obj):
        user = obj.salesman.status
        return user == 'Модератор'


class IsSalesmanUpdate(BasePermission):
    """
    Кастомные права доступа для обновления Товара, только Продавцом который его создал
    """
    message = "Вы не являетесь продавцом данного товара"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.salesman
