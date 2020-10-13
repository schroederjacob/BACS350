from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
# from .models import Superhero

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
