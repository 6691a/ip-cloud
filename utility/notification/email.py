from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email(subject: str, message: str, from_email: str, recipient_list: list, **kwargs):
    """
    Send email to recipient list
    """
    send_mail(subject, message, from_email, recipient_list, **kwargs)
