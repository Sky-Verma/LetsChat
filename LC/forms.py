from .models import User_Info
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class updateForm(ModelForm):
    
    class Meta:
        model=User_Info
        fields='__all__'
        exclude=['user']


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','email','first_name','last_name','password2']

   


   