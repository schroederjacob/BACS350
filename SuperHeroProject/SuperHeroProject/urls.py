from django.contrib import admin
from django.urls import path
from Hero.views import HeroView, IndexView, HeroAddView, HeroListView, HeroEditView, HeroDetailView, HeroDeleteView

urlpatterns = [
    # path('', IndexView.as_view()),
    # path('index', IndexView.as_view()),
    # path('<str:identity>', HeroView.as_view()),
    path('', HeroListView.as_view(), name='HeroList'),
    path('admin/', admin.site.urls),
    path('add', HeroAddView.as_view(), name='AddHero'),
    path('<int:pk>/', HeroEditView.as_view(), name='EditHero'),
    path('<int:pk>', HeroDetailView.as_view(), name='HeroDetail'),
    path('<int:pk>/delete', HeroDeleteView.as_view(), name='DeleteHero')
]
