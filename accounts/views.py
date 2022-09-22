from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            messages.success(request, "SIGNUP SUCCESS!")
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

