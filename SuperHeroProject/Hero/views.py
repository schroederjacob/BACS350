from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Superhero
from django.urls import reverse_lazy
from .forms import SuperheroForm
from django.http import HttpResponseRedirect

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
    context_object_name = 'object'
    

class HeroListView(ListView):
    template_name = "HeroList.html"
    model = Superhero

class HeroDeleteView(DeleteView):
    template_name = "DeleteHero.html"
    success_url = reverse_lazy('hero_list')

class SuperheroImage(TemplateView):
    form = SuperheroForm
    template_name = 'heroimage.html'

    def post(self, request, *args, **kwargs):
        form = SuperheroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('home', kwargs={'pk': pk}))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
