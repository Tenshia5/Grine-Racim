from django.db import models

class Proprietaire(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    num_phone = models.IntegerField()
    adresse = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos=%Y/%m/%d/')
    is_vet = models.BooleanField(default=False)
    

    def __str__(self):
        return self.nom