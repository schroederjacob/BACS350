from django.contrib import admin
from django.urls import path
from pages.views import HomeView, BasePage, HeroView

urlpatterns = [
    path('', HeroView.as_view()),
    path('<str:identity>', = HeroView.as_view())
]
