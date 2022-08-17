from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render


class UserLoginView(LoginView):
    template_name = 'app_users/login.html'


class UserLogoutView(LogoutView):
    template_name = 'app_users/logout.html'
