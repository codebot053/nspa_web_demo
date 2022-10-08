from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    path('login/', views.login, name='login'), # /accounts/login => conf.global_settings.LOGIN_URL
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path("password_change/", views.password_change, name="password_change"),
    re_path(r'^(?P<username>[\w.@+-]+)/',views.profile_view, name="profile"),
]
