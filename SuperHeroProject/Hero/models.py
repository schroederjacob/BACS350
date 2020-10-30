from django.db import models

# Add models here.
class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
    image = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.identity

    def get_absolute_url(self): 
        return reverse('HeroDetail', args=[str(self.id)])
