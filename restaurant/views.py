from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Categoria, Plato
from .serializers import CategoriaSerializer, PlatoSerializer, PlatoDetailSerializer

# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
    @action(detail=True, methods=['get'])
    def platos(self, request, pk=None):
        """Obtener todos los platos de una categoría específica"""
        try:
            categoria = self.get_object()
            platos = Plato.objects.filter(categoria=categoria)
            serializer = PlatoSerializer(platos, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PlatoDetailSerializer
        return PlatoSerializer
    
    def update(self, request, *args, **kwargs):
        """Personalización para manejar actualizaciones sin imagen"""
        plato = self.get_object()
        
        # Si no se envía una imagen, usamos la existente
        if 'imagen' not in request.data or not request.data['imagen']:
            # Quitamos imagen del request para que no se valide
            data = request.data.copy()
            data.pop('imagen', None)
            serializer = self.get_serializer(plato, data=data, partial=True)
        else:
            serializer = self.get_serializer(plato, data=request.data)
            
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def destacados(self, request):
        """Obtener platos destacados"""
        platos = Plato.objects.filter(destacado=True)
        serializer = self.get_serializer(platos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def por_categoria(self, request):
        """Filtrar platos por categoría"""
        categoria_id = request.query_params.get('categoria_id', None)
        if categoria_id:
            platos = Plato.objects.filter(categoria_id=categoria_id)
            serializer = self.get_serializer(platos, many=True)
            return Response(serializer.data)
        return Response({'error': 'Se requiere un ID de categoría'}, status=status.HTTP_400_BAD_REQUEST)
