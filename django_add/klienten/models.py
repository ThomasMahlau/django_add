from django.db import models

# Create your models here.

class Klienten(models.Model):
    name = models.CharField(max_length=100, null=True)
    vorname = models.CharField(max_length=100, null=True)
    strasse = models.CharField(max_length=100, null=True)
    plz = models.CharField(max_length=100, null=True)
    ort = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name
