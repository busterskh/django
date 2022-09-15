from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    phone = forms.IntegerField()
    city = forms.CharField(max_length=50)
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')


# class UpdateForm(forms.Form):
#     phone = forms.IntegerField()
#     city = forms.CharField(max_length=50)
#     avatar = forms.ImageField()
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)


class UpdateFormView(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = Profile
        fields = ['phone', 'city', 'avatar']
