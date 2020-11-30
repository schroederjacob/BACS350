from django.contrib import admin
from django.urls import path
from Hero.views import HeroView, IndexView, HeroAddView, HeroListView, HeroEditView, HeroDetailView, HeroDeleteView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from Hero import views as user_views

urlpatterns = [
    # path('', IndexView.as_view()),
    # path('index', IndexView.as_view()),
    # path('<str:identity>', HeroView.as_view()),
    path('', HeroListView.as_view(), name='HeroList'),
    path('admin/', admin.site.urls),
    path('add', HeroAddView.as_view(), name='AddHero'),
    path('<int:pk>/', HeroEditView.as_view(), name='EditHero'),
    path('<int:pk>', HeroDetailView.as_view(), name='HeroDetail'),
    path('<int:pk>/delete/', HeroDeleteView.as_view(), name='DeleteHero'),
    path('register/', user_views.Register, name='Register'),
    path('profile/', user_views.Profile, name='Profile'),
    path('login/', auth_views.LoginView.as_view(template_name='Login.html'), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Logout.html'), name='Logout')
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
