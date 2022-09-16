from .models import User
from django import forms    


class SignupForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['username', 'password', 'email']   