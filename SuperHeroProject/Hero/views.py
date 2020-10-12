from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Superhero

class HeroView(TemplateView):
    template_name = "Hero.html"

    def get_context_data(self, **kwargs):
        hero = Superhero.objects.all()
#        heroes = ['SpiderMan', 'CaptainAmerica', 'IronMan', 'Daredevil', 'Wolverine']
        return {'hero': hero}

class IndexView(TemplateView):
    template_name = "index.html"
