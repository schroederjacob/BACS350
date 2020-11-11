from django.contrib import admin
from django.urls import path
from Hero.views import HeroView, IndexView, HeroAddView, HeroListView, HeroEditView, HeroDetailView, HeroDeleteView
from django.conf.urls.static import static
from django.conf import settings

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

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
