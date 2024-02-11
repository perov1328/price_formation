from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админка для пользователей
    """
    list_display = ('first_name', 'last_name', 'email', 'status',)
    list_filter = ('status',)
