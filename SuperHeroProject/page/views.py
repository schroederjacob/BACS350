from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

class HeroView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        heroes = Superhero.objects.all()
        return {'heroes': heroes}
 
class AddHeroView(CreateView):
    template_name = "addhero.html"
    model = Superhero
    

class BasePage(TemplateView):
    template_name = "pagetheme.html"
    
    
class AboutPage(TemplateView):
    template_name = "about.html"
