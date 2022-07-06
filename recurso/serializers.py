
from recurso.models import Estado, Marca, Modelo, RecursoTecnologico, TipoRecursoTecnologico
from rest_framework import serializers

class TipoRecursoTecnologicoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoRecursoTecnologico
        fields = ['id', 'nombre', 'descripcion']
        read_only_fields = ['id'] 

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre']
        read_only_fields = ['id']


class ModeloSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()
    
    class Meta:
        model = Modelo
        fields = ['id', 'nombre','marca']
        read_only_fields = ['id']
    

class RecursoTecnologicoSerializer(serializers.ModelSerializer):
    tipoRecurso = TipoRecursoTecnologicoSerializer()
    modelo = ModeloSerializer()


    class Meta:
        model = RecursoTecnologico
        fields = ['id','numeroRT', 'tipoRecurso', 'modelo']
        read_only_fields = ['id']   

class EstadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Estado
        fields = ['id', 'nombre', 'ambito', 'reservable', 'esCancelable' ]
        read_only_fields = ['id']