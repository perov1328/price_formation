from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    """
    Кастомные права доступа для обновления Профиля, только человеком который его создал
    """
    message = "Вы не можете просматривать чужие учетные записи."

    def has_object_permission(self, request, view, obj):
        return request.user == obj
