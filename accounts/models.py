from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import resolve_url
from django.template.loader import render_to_string
from django.urls import reverse

class User(AbstractUser):
    # 각 변수에 할당되는 첫번째 값은 DB에 저장되는 값이고 두번째 값은 보여지는 값이다.
    class GenderChoices(models.TextChoices):
        MALE = "M", "남자"
        FEMALE = "F", "여자"

    # 소개
    bio = models.TextField(blank=True)
    # 정규표현식에서 010 다음에는 1-9 까지의 숫자중 하나 그리고 0-9 까지 3번 반복 
    phone_number = models.CharField(max_length=13, validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")] ,blank=True)
    # default=GenderChoices.MALE 를 default 로 주게되면 기본값으로 "M"이 할당된다.
    gender = models.CharField(max_length=4,choices=GenderChoices.choices ,blank=True)
    # models.ImageField 의 경우도 DB에는 경로를 저장하게 된다. CharField 로 볼 수 있다.
    profile_image = models.ImageField(blank=True, upload_to="accounts/profile/%Y/%m/%d")
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def profile_image_url(self):
        if self.profile_image:
            return self.profile_image.url

        else:
            return resolve_url("pydenticon_image", self.username)

    def send_welcome_email(self):
        user_name = self.first_name
        subject = f"{user_name}님 DEV_TOYBOX 가입을 환영합니다."
        # context 값으로 user를 넘겨줌.
        content = render_to_string("accounts/welcome_email_content.txt", {
            "user":self
            })
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail(subject, content, sender_email, [self.email], fail_silently=False)
    
    