from django.contrib import admin
from django.urls import path
from pages.views import HeroView

urlpatterns = [
    path('', HeroView.as_view()),
    path('<str:identity>', = HeroView.as_view())
]
