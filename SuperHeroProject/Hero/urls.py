from django.contrib import admin
from django.urls import path
from Hero.views import HeroView, IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    # path('index', IndexView.as_view()),
    path('<str:identity>', HeroView.as_view())

]
