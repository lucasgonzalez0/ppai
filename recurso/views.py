from django.shortcuts import render
from django.shortcuts import get_object_or_404
from recurso.serializers import EstadoSerializer, MarcaSerializer, ModeloSerializer, RecursoTecnologicoSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from recurso.models import Estado, GestorIngresoMantenimiento, Marca, Modelo, RecursoTecnologico
from rest_framework.views import APIView
from rest_framework import generics




class RecursoTecnologicoViewSet(viewsets.ModelViewSet):
    """
    Vista para agregar un Llamada.
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = RecursoTecnologicoSerializer
    http_method_names = ['get', 'post','put', 'head', 'options']
  
    def get_queryset(self):
        return RecursoTecnologico.objects.all()

    def list(self, request):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        puntoDeVenta = serializer.data
        return Response(data=puntoDeVenta, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data.copy()
        serializer = self.get_serializer_class()(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

class EstadoViewSet(viewsets.ModelViewSet):
    """
    Vista para agregar un Llamada.
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = EstadoSerializer
    http_method_names = ['get', 'post','put', 'head', 'options']
  
    def get_queryset(self):
        return Estado.objects.all()

    def list(self, request):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        puntoDeVenta = serializer.data
        return Response(data=puntoDeVenta, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data.copy()
        serializer = self.get_serializer_class()(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

class MarcaViewSet(viewsets.ModelViewSet):
    """
    Vista para agregar un Llamada.
    """
    serializer_class = MarcaSerializer
    http_method_names = ['get', 'post','put', 'head', 'options']
  
    def get_queryset(self):
        return Marca.objects.all()

    def list(self, request):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        puntoDeVenta = serializer.data
        return Response(data=puntoDeVenta, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data.copy()
        serializer = self.get_serializer_class()(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

class ModeloViewSet(viewsets.ModelViewSet):
    """
    Vista para agregar un Llamada.
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = ModeloSerializer
    http_method_names = ['get', 'post','put', 'head', 'options']
  
    def get_queryset(self):
        return Modelo.objects.all()

    def list(self, request):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        puntoDeVenta = serializer.data
        return Response(data=puntoDeVenta, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data.copy()
        serializer = self.get_serializer_class()(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

class RecursoTecnologicoDisponible(generics.ListAPIView):
    serializer_class = RecursoTecnologicoSerializer

    def get_queryset(self):
        # Recuros disponibles
        return RecursoTecnologico.objects.all()


class VerificarTurnoDisponible(APIView):
    

    def post(self, request):
        # Recuros disponibles
        print(request)
        gm = GestorIngresoMantenimiento(request)
        data = gm.verificarTurno()
        # gm.agruparRTPorTipoDeRecurso(data)
        return Response(data, status=status.HTTP_200_OK)

   