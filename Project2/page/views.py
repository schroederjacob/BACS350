from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class SpiderManView(TemplateView):
    template_name = 'spiderman.html'

class CapAmericaView(TemplateView):
    template_name = 'captainamerica.html'
