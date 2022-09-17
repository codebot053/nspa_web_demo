from django import forms
from django.contrib.auth.forms import UserCreationForm    
from .models import User


class SignupForm(UserCreationForm):
    #기존 UserCreationForm 의 Meta를 overwrite 해 버리기에 Meta도 상속받는다.
    class Meta(UserCreationForm.Meta): 
        model = User
        fields = ['username','first_name','last_name', 'email']   