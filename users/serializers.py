from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Пользователя
    """
    password = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'city', 'first_name', 'last_name', 'password',)


class UserViewSerializer(serializers.ModelSerializer):
    """
    Сериализатор для просмотра модели Пользователя
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'city',)


class MessageSerializer(serializers.Serializer):
    """
    Сериализатор для отправки сообщения в ТП
    """
    email = serializers.EmailField(required=True)
    subject = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=1000)

    class Meta:
        fields = ('email', 'subject', 'message',)
