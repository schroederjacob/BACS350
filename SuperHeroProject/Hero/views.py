from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Superhero
from django.urls import reverse_lazy

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

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)
    

class HeroEditView(UpdateView):
    template_name = "EditHero.html"
    model = Superhero
    fields = '__all__'

    

class HeroDetailView(DetailView):
    template_name = "HeroDetail.html"
    model = Superhero

class HeroListView(ListView):
    template_name = "HeroList.html"
    model = Superhero

class HeroDeleteView(DeleteView):
    template_name = "DeleteHero.html"
    success_url = reverse_lazy('hero_list')
