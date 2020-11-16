from django.db import models
from django.urls import reverse

# Add models here.
class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
    ## image = models.ImageField(default='placeholder.jpg',upload_to='upload/')
    image = models.CharField(max_length=80)
    
    def __str__(self):
        return self.identity

    def get_absolute_url(self): 
        return reverse('HeroDetail', args=[str(self.id)])
