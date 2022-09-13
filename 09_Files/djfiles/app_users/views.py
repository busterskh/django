from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateForm
from .models import Profile
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView


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


def update_form(request, pk):
    profile = Profile.objects.get(id=pk)

    if request.user == profile.user:
        if request.method == 'POST':
            form = UpdateForm(request.POST, request.FILES)
            if form.is_valid():
                profile.phone = form.cleaned_data.get('phone')
                profile.city = form.cleaned_data.get('city')
                profile.avatar = form.cleaned_data.get('avatar')
                profile.save()

                user = profile.user
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.save()
                return redirect(f'/user/{pk}/')
        else:
            form = UpdateForm()
    else:
        HttpResponse(content='Доступ запрещен.', status=403)

    context = {'form': form}
    return render(request, 'app_users/edit.html', context=context)


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'app_users/user_profile.html'


