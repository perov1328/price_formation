from django.conf import settings
from django.core.mail import send_mail


def send_support_message(subject, message):
    """
    Функция для отправки письма в службу поддержки
    :param subject: Тема письма
    :param message: Текст письма
    :return: None
    """
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_SUPPORT_USER]
    )
