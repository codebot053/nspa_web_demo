from django import forms
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm as AuthPasswordChangeForm)
from .models import User


class SignupForm(UserCreationForm):
    #기존 UserCreationForm 의 Meta를 overwrite 해 버리기에 Meta도 상속받는다.

    def __init__(self, *args, **kwargs):# 생성자
        super().__init__(*args, **kwargs) # 원래의 부모 호출
        self.fields['email'].required = True #필드값 무조건 요구하도록 수정
        # self.fields['first_name'].required = True
        # self.fields['last_name'].required = True

    class Meta(UserCreationForm.Meta): 
        model = User
        # fields = ['username', 'email', 'first_name','last_name'] 
        fields = ['username', 'email']

    def clean_email(self): 
        email = self.cleaned_data.get('email')
        print(email)
        if email:
            qs = User.objects.filter(email=email)
            print(qs)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image', 'first_name', 'last_name', 'email', 'bio', 'phone_number', 'gender']

class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password2(self):
        old_password = self.cleaned_data.get('old_password')
        new_password2 = super().clean_new_password2()
        if old_password == new_password2:
            raise forms.ValidationError("새로 지정하실 password는 기존의 password와 다르게 입력해 주세요.")
        return new_password2
    
    