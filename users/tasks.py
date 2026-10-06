from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import logging

from .models import CustomUser
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


logger = logging.getLogger(__name__)

@shared_task
def send_welcome_email(email, first_name):
    subject = 'Welcome to Second Hand!'
    message = f"""
    Hi {first_name},

    Thank you for registering at Second Hand. 
    """

    html_message = f"""
    <h1> Welcome , {first_name}!</h1>
    <p> Thank you for registering at Second Hand. </p>
    """

    try: 
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
            html_message=html_message,
        )
        logger.info(f"Welcome email sent to {email}")
    except Exception as e:
        logger.error(f"Failed to send welcome email to {email}: {str(e)}") 
        raise


@shared_task
def send_password_reset_email(email, user_id):

    logger.info(f"Starting password reset email task for user_id: {email}, user_is={user_id}")
    try:
        user = CustomUser.objects.get(pk=user_id)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_url = f"{settings.SITE_URL}{reverse('users:password_reset_confirm', kwargs={'uidb64': uid, 'token': token})}"
        subject = 'Password Reset Request'
        message = f"""
        Hi {user.first_name },

        You requested a password reset. Click the link below to reset your password:
        {reset_url}

        If you did not request this, please ignore this email.
        """
        html_message = f"""
        <h1>Password Reset Request</h1>
        <p>Hi {user.first_name},</p>
        <p>You requested a password reset. Click the link below to reset your password:</p>
        <a href="{reset_url}">Reset Password</a>
        <p>If you did not request this, please ignore this email.</p>
        """

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
            html_message=html_message,
        )
        logger.info(f"Password reset email sent to {email}")
    except Exception as e:
        logger.error(f"Failed to send password reset email to {email}: {str(e)}")
        raise