from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mitarbeiter(models.Model):
    benutzer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    vorname = models.CharField(max_length=100, null=True)
    strasse = models.CharField(max_length=100, null=True)
    plz = models.CharField(max_length=100, null=True)
    ort = models.CharField(max_length=100, null=True)
    geburtsdatum = models.DateField(null=True, blank=True)
    einstellungsdatum = models.DateField(null=True, blank=True)
    telefonnummer = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name
    
class Navigation(models.Model):
    nav_punkt = models.CharField(max_length=100, null=True)
    nav_text = models.TextField(null=True)
    nav_link = models.CharField(max_length=100, null=True)
    nav_image = models.ImageField(null=True)
    
    def __str__(self):
        return self.nav_punkt