from product.constants import TAX, BANK_COMMISSION, SELLER_COMMISSION, PLATFORM_COMMISSION


def price_formation(self, serializer):
    """
    Функция для расчета итоговой стоимости товара
    """
    data = serializer.validated_data
    data['salesman'] = self.request.user
    data['sellers_price'] = float(data['sellers_price'])
    data['tax'] = data['sellers_price'] * TAX
    data['bank_commission'] = data['sellers_price'] * BANK_COMMISSION
    data['seller_commission'] = data['sellers_price'] * SELLER_COMMISSION
    data['platform_commission'] = data['sellers_price'] * PLATFORM_COMMISSION
    data['total_price'] = sum(data[field] for field in ['sellers_price', 'tax', 'bank_commission',
                                                        'seller_commission', 'platform_commission'])
    serializer.save()


def price_formated_for_sale(self, serializer):
    """
    Функция для расчета стоимости товара в случае попадания его на распродажу
    """
    price_formation(self, serializer)
    data = serializer.validated_data
    if data['sale']:
        data['price_discount'] = (float(data['total_price']) -
                                  (float(data['total_price']) * data['discount_percentage']))
    elif not data['sale']:
        data['discount_percentage'] = 0
        data['price_discount'] = data['total_price']
    serializer.save()
