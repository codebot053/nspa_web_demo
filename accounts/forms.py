from django import forms
from django.contrib.auth.forms import UserCreationForm    
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