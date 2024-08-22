from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Users
from django.http.response import HttpResponse
from django.forms.models import ModelForm

class UserForm(ModelForm):
    class Meta:
        model=Users
        fields='__all__'
class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']