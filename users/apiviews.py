from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from users.models import User
from users.permissions import IsUser
from users.serializers import UserSerializer, UserViewSerializer, MessageSerializer
from users.services import send_support_message
from rest_framework.response import Response
from rest_framework import status


class UserCreateAPIView(CreateAPIView):
    """
    Контроллер для создания сущности моедли Пользователя
    """
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотора конкретной сущности модели Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserViewSerializer
    permission_classes = [IsUser]


class UserUpdateAPIView(UpdateAPIView):
    """
    Контроллер для обновления сущности модели Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUser]


class UserDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаления сущности модели Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUser | IsAdminUser]


class SupportMessage(APIView):
    """
    Контроллер для отправки сообщения в тех. поддержку
    """
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['email'] = request.user.email
        serializater = MessageSerializer(data=data)
        if serializater.is_valid():
            send_data = serializater.data
            send_data['message'] += "\n\n" + send_data['email']
            send_support_message(send_data['subject'], send_data['message'])
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(self.serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
