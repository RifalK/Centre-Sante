from django.db import models
from centresante.models import *

class Patient(models.Model):

    id = models.BigAutoField(primary_key=True)
    nom     = models.CharField(max_length=200)
    prenom     = models.CharField(max_length=255)
    code_patient     = models.Aggregate(max_length=20)
    sexe     = models.CharField(max_length=50)
    date_naissance = models.DateField(max_length=100)
    numero_mobile    = models.PositiveBigIntegerField()
    numero_telephone    = ''
    isn    = ''
    residence_habituelle = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    Professionnelsante = models.ForeignKey("Professionnelsante", on_delete=models.SET_NULL, null=True, related_name="Patient")
    religion = models.CharField(null=True)
    profession = models.CharField(null=True)
    residence_actuelle = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    pere = ''
    mere = ''
    autre_ethnie = ''

    def __unicode__(self):
        return "{0}".format(self.nom, self.Professionnelsante)
    
class Professionnelsante(models.Model):

    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=250)
 
    def __unicode__(self):
        return "{0}".format(self.first_name, self.last_name )


