from django import forms
from .models import Superhero, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Superhero model
class SuperheroForm(forms.ModelForm):
    class Meta:
        model = Superhero
        fields = ['name', 'identity', 'image']

# Profile model
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


