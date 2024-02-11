from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from users.models import User
from product.constants import TAX, BANK_COMMISSION, SELLER_COMMISSION, PLATFORM_COMMISSION


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

    def test_product_create_zero_cost(self):
        """
        Тестирование создание продукта со стоимостью равной или меньше нуля
        """

        # Нулевая стоимость
        data_1 = {
            'title': 'test 1',
            'description': 'test 1',
            'sellers_price': 0,
        }
        response_1 = self.client.post(
            reverse('products:product_create'),
            data=data_1
        )
        self.assertEqual(
            response_1.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        # Стоимость меньше нуля
        data_2 = {
            'title': 'test 1',
            'description': 'test 1',
            'sellers_price': -100,
        }
        response_2 = self.client.post(
            reverse('products:product_create'),
            data=data_2
        )
        self.assertEqual(
            response_2.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_product_create_calculation(self):
        """
        Тестирование создания Продукта и проверка расчетов итоговой стоимости и издержек
        """
        data = {
            'title': 'test 1',
            'description': 'test 1',
            'sellers_price': 100,
        }
        response = self.client.post(
            reverse('products:product_create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        tax = data['sellers_price'] * TAX
        self.assertEqual(response.data['tax'], tax)
        bank_commission = data['sellers_price'] * BANK_COMMISSION
        self.assertEqual(response.data['bank_commission'], bank_commission)
        seller_commission = data['sellers_price'] * SELLER_COMMISSION
        self.assertEqual(response.data['seller_commission'], seller_commission)
        platform_commission = data['sellers_price'] * PLATFORM_COMMISSION
        self.assertEqual(response.data['platform_commission'], platform_commission)
        total_price = data['sellers_price'] + tax + bank_commission + seller_commission + platform_commission
        self.assertEqual(response.data['total_price'], total_price)

    def test_product_create_user(self):
        """
        Тестирование создания продукта пользователем без статуса Продавец
        """
        self.user_new = User.objects.create(
            email='test123@yandex.ru',
            password='test12345',
            status='User'
        )
        self.client_user = APIClient()
        self.client_user.force_authenticate(user=self.user_new)
        data = {
            'title': 'test 1',
            'description': 'test 1',
            'sellers_price': 100,
        }
        response = self.client_user.post(
            reverse('products:product_create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_product_update(self):
        """
        Тестирование обновления продукта
        """
        data = {
            'title': 'test 1',
            'description': 'test 1',
            'sellers_price': 100,
        }
        response = self.client.post(
            reverse('products:product_create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        update_url = reverse('products:product_update', args=[response.data['id']])
        update_data = {
            'sellers_price': 200,
            'sale': True,
            'discount_percentage': 0.1
        }
        response_2 = self.client.patch(update_url, update_data, format='json')
        self.assertEqual(
            response_2.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(response_2.data['sale'], True)
        self.assertEqual(response_2.data['discount_percentage'], 0.1)
        price_discount = (float(response_2.data['total_price']) -
                          (float(response_2.data['total_price']) * response_2.data['discount_percentage']))
        self.assertEqual(response_2.data['price_discount'], price_discount)
