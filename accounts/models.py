from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string

class User(AbstractUser):
    bio = models.TextField(blank=True)

    def send_welcome_email(self):
        user_name = self.first_name
        subject = f"{user_name}님 DEV_TOYBOX 가입을 환영합니다."
        # context 값으로 user를 넘겨줌.
        content = render_to_string("accounts/welcome_email_content.txt", {
            "user":self
            })
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail(subject, content, sender_email, [self.email], fail_silently=False)