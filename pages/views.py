from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = '/templates/home.html'

class AboutView(TemplateView):
    template_name = '/templates/about.html'
