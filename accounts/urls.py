from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

app_name='accounts'

urlpatterns = [
    path('login/', views.login, name='login'), # /accounts/login => conf.global_settings.LOGIN_URL
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    

]
