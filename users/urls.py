from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.urls import path
from users.apps import UsersConfig
from users.apiviews import UserCreateAPIView, UserRetrieveAPIView, UserDeleteAPIView, UserUpdateAPIView, SupportMessage


app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('support/', SupportMessage.as_view(), name='support_message')
]
