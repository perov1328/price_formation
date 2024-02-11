from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from users.models import User


class ProductTestCase(APITestCase):
    """
    Тестирование модели Продукта
    """
    def setUp(self):
        self.user = User.objects.create(
            email='test1@yandex.ru',
            password='test12345',
            status='Salesman'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_support_message(self):
        """
        Тестирование отправки сообщения в службу поддержки
        """
        url = reverse('users:support_message')
        data = {
            'subject': 'Test',
            'message': 'Test',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.data,
            None
        )
