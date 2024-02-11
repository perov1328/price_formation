from product.apps import ProductConfig
from django.urls import path
from product.apiviews import (ProductListAPIView, ProductCreateAPIView, ProductRetrieveAPIView,
                              ProductUpdateAPIView, ProductDeleteAPIView)

app_name = ProductConfig.name

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product_list'),
    path('create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product_delete'),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product_update'),
]
