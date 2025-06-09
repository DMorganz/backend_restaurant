from rest_framework import serializers
from .models import Categoria, Plato

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class PlatoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')
    imagen = serializers.ImageField(required=False)
    
    class Meta:
        model = Plato
        fields = '__all__'
        
class PlatoDetailSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    
    class Meta:
        model = Plato
        fields = '__all__' 