from rest_framework import serializers
from centresante.models import *

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient 
        fields = ('id', 'nom', 'prenom', 'code_patient', 'sexe', 'date_naissance', 'numero_mobile', 'isn', 'numero_telephone','Professionnelsante_id', 'residence_habituelle', 'create_at', 'religion', 'profession', 'residence_actuelle', 'email', 'pere', 'mere', 'autre_ethnie')


class ProfessionnelsanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professionnelsante
        fields = ('id', 'first_name', 'last_name')
