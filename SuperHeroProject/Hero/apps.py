from django.apps import AppConfig

class HeroConfig(AppConfig):
    name = 'Hero'

    def ready(self):
        import users.signals
