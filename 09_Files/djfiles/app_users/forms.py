from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    phone = forms.IntegerField()
    city = forms.CharField(max_length=50)
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')


class UpdateProfileForm(forms.ModelForm):
    phone = forms.IntegerField()
    city = forms.CharField(max_length=50)
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
