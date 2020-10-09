from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

class HeroView(TemplateView):
    template_name = "Hero.html"

    def get_context_data(self, **kwargs):
        heroes = Superhero.objects.all()
        return {'heroes': heroes}
 
class AddHeroView(CreateView):
    template_name = "AddHero.html"
    model = Superhero
    

class BasePage(TemplateView):
    template_name = "PageTheme.html"
    
    
class AboutPage(TemplateView):
    template_name = "About.html"
