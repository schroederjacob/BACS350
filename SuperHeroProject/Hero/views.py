from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Superhero, Profile
from django.urls import reverse_lazy, reverse
from .forms import SuperheroForm, RegisterForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User
from django import forms

class HeroView(TemplateView):
    template_name = "Hero.html"

    def get_context_data(self, **kwargs):
        id = kwargs.get('identity', 'SpiderMan')
#       heroes = ['SpiderMan', 'CaptainAmerica', 'IronMan', 'Daredevil', 'Wolverine']
        return {'hero': id, 'css': '/static/style.css'}

class IndexView(TemplateView):
    template_name = "index.html"
                        
class BaseView(TemplateView):
    template_name = "SuperHeroTheme.html"

class HeroAddView(CreateView):
    template_name = "AddHero.html"
    model = Superhero
    fields = '__all__'

class HeroEditView(UpdateView):
    template_name = "EditHero.html"
    model = Superhero
    fields = '__all__' 

class HeroDetailView(DetailView):
    template_name = "HeroDetail.html"
    model = Superhero
    context_object_name = 'hero'

class HeroListView(ListView):
    template_name = "HeroList.html"
    model = Superhero
    context_object_name = 'heroes'

class HeroDeleteView(DeleteView):
    template_name = "DeleteHero.html"
    model = Superhero
    success_url = reverse_lazy('HeroList')

## class RegisterView(CreateView):
    ## template_name = "Register.html"
    ## form_class = UserCreationForm
    ## success_url = reverse_lazy('Login')

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('Login')
    else:
        form = RegisterForm()
    return render(request, 'Register.html', {'form': form})

@login_required
def Profile(request):
    return render(request, 'Profile.html')

## class ProfileView(TemplateView):
    ## template_name = "Profile.html"
    ## model = Profile
    ## context_object_name = 'user'
