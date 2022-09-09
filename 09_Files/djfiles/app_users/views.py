from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateProfileForm
from .models import Profile
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView


class UserLoginView(LoginView):
    template_name = 'app_users/login.html'


class UserLogoutView(LogoutView):
    template_name = 'app_users/logout.html'


class ProfileCreate(CreateView):
    model = Profile
    template_name = 'app_users/registration.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        phone = form.cleaned_data.get('phone')
        city = form.cleaned_data.get('city')
        avatar = self.request.FILES['avatar']
        Profile.objects.create(
            user=user,
            city=city,
            phone=phone,
            is_verification=False,
            id=user.id,
            avatar=avatar,
        )
        return super().form_valid(form)

    success_url = reverse_lazy('login')


class UpdateProfile(UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'app_users/edit.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('all_news')

    def get_context_data(self, **kwargs):
        data = super(UpdateProfile, self).get_context_data(**kwargs)
        data['user'] = self.request.user
        return data

    def test_func(self):
        profile = self.get_object()
        return profile.user == self.request.user


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'app_users/user_profile.html'


