from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.views import( LoginView, logout_then_login,
     PasswordChangeView as AuthPasswordChangeView)
from .forms import SignupForm, ProfileForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

login = LoginView.as_view(template_name="accounts/login_form.html")
# logout = LogoutView.as_view()
def logout(request):
    messages.success(request, "로그아웃 되었습니다.")
    return logout_then_login(request)


# @login_required
def profile_view(request, username):
    # username=list(username)
    # username.pop(-1)
    # username = ''.join(username)
    # user_profile = get_user_model().objects.get(username=username)
    # return render(request, "accounts/profile.html",{"user_profile":user_profile})

    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    return render(request, "accounts/profile.html",{
        "page_user":page_user,
    })




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
    return render(request, "accounts/profile_edit.html",
    {
        "form":form
    })
# @login_required
# def password_change(request):
#     pass

class PasswordChangeView(LoginRequiredMixin,AuthPasswordChangeView):
    success_url= reverse_lazy("accounts:password_change")
    template_name = 'accounts/password_change_form.html'
    form_class = PasswordChangeForm
    # FormView를 통해 form 객채를 인자로 전달 받는다.
    def form_valid(self, form):
        messages.success(self.request , "PW를 변경했습니다.")
        return super().form_valid(form)

password_change = PasswordChangeView.as_view()

