from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(label = "Full name")


    class Meta:
        model = User
        fields=('first_name', 'username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields=['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']
