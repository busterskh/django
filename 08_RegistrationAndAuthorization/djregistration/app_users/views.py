from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from app_users.forms import RegisterForm
from app_users.models import Profile
from django.views.generic import DetailView


class UserLoginView(LoginView):
    template_name = 'app_users/login.html'


class UserLogoutView(LogoutView):
    template_name = 'app_users/logout.html'


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone = form.cleaned_data.get('phone')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                phone=phone,
                is_verification=False,
                id=user.id
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'app_users/registration.html', {'form': form})


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'app_users/user_profile.html'

