from dataclasses import field
from django import forms
from django.forms import EmailField, ModelForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm, ModelForm ):
    #UserCreationForm doesn't come with and email so this line adds an email field to the form
    email = forms.EmailField(required=True)
    class Meta:
        model= User
        fields = ['username', 'email', 'password1','password2']