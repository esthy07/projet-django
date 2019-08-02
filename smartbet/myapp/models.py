from django.db import models

# Create your models here.

class Internaute(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)


class Pari(models.Model):
    numero = models.CharField(max_length = 50)
    internaute = models.ForeignKey(Internaute, on_delete='pari')

class choix(models.Model):
    id_user = models.ForeignKey(Internaute, on_delete='pari')
    heure = models.DateTimeField(auto_now_add = True)

class user(models.Model):
    username = models.CharField(max_length= 50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
