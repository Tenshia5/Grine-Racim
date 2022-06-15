from unicodedata import decimal
from xml.dom import NoModificationAllowedErr
from django.db import models
from proprietaires.models import Proprietaire
from datetime import datetime

class Carnet(models.Model):
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.DO_NOTHING)
    nom = models.CharField(max_length=100)
    espece = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    sexe = models.CharField(max_length=100)
    couleur = models.CharField(max_length=100)
    pedigre = models.BooleanField(default=True)
    sterilise = models.BooleanField(default=True)

    num_id = models.CharField(max_length=200)
    type_id = models.CharField(max_length=200)
    place_id = models.CharField(max_length=200)

    date_nais = models.DateTimeField()
    poids_nais = models.DecimalField(max_digits=3, decimal_places=3)
    taille_nais = models.DecimalField(max_digits=4, decimal_places=2)
    lieu_nais = models.CharField(max_length=200)

    description = models.TextField(blank=True)
    comportement = models.TextField(blank=True)
    antecedants = models.TextField(blank=True)
    assurance = models.TextField(blank=True)

    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)

    def __str__(self):
        return self.nom

class Consultation(models.Model):
    nom = models.ForeignKey(Carnet, on_delete=models.DO_NOTHING)
    date_cons = models.DateTimeField(default=datetime.now, blank=True)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    note = models.CharField(max_length=200)
    poids_cons = models.DecimalField(max_digits=6, decimal_places=3)
    taille_cons = models.DecimalField(max_digits=4, decimal_places=2)


class CalVac(models.Model):
    nom = models.ForeignKey(Carnet, on_delete=models.DO_NOTHING)
    date_vac = models.DateTimeField()
    daterappel_vac = models.DateTimeField()
    vaccin = models.CharField(max_length=200)
    observations = models.CharField(max_length=200,blank=True)
    praticien = models.CharField(max_length=200)



    #date_arrive = models.DateTimeField()
    #poids_arrive = models.DecimalField(max_digits=3, decimal_places=3)
    #taille_arrive = models.DecimalField(max_digits=2, decimal_places=2)
    #eleveur = models.CharField(max_length=200)

    #date_depart = models.CharField(max_length=200)
    #poids_depart = models.DecimalField(max_digits=3, decimal_places=3)
    #taille_depart = models.DecimalField(max_digits=2, decimal_places=2)
    #type = models.CharField(max_length=200)
    
