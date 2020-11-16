from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Superhero
from django.urls import reverse_lazy, reverse
from .forms import SuperheroForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

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
