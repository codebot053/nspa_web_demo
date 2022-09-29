from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, logout_then_login, LogoutView
from .forms import SignupForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login

login = LoginView.as_view(template_name="accounts/login_form.html")
# logout = LogoutView.as_view()
def logout(request):
    messages.success(request, "로그아웃 되었습니다.")
    return logout_then_login(request)



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            print(type(signed_user))
            auth_login(request, signed_user)
            messages.success(request, "회원가입 되었습니다.")
            signed_user.send_welcome_email() # FIXME : celery로 비동기 처리하는것을 추천
             # get 인자 next 를 받아오고 없으면 다음 지정된 '/' url 로 다음 url 지정
             # 그리고 '/' 자리에 url , url pattern name 을 사용해도 된다.
             # redirect 가 먼저 url pattern name으로 시도해보고 없으면 url 로 시도해본다.
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form' : form,
    })

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필 수정했습니다.")
            return redirect("accounts:profile_edit")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile_edit.html",{"form":form
        
    })
    
