from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """
    Кастомная команда для создания супер пользователя
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='perov97@yandex.ru',
            first_name='Alexander',
            last_name='Perov',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password('egoradm1')
        user.save()
