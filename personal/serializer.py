
from personal.models import AsignacionResponsableTecnicoRT, PersonalCientifico
from rest_framework import serializers

class PersonalCientificoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalCientifico
        fields = ['id', 'nombre']
        read_only_fields = ['id']


class AsignacionResponsableSerializer(serializers.ModelSerializer):
    personal = PersonalCientificoSerializer()
    
    class Meta:
        model = AsignacionResponsableTecnicoRT
        fields = ['id', 'fechaDesde', 'personal']
        read_only_fields = ['id']