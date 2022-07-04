from django.shortcuts import render

from personal.models import AsignacionResponsableTecnicoRT, PersonalCientifico
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets

from personal.serializer import AsignacionResponsableSerializer, PersonalCientificoSerializer


# Create your views here.

class PersonalCientificoViewSet(viewsets.ModelViewSet):
    """
    Vista para agregar un Llamada.
    """
    serializer_class = PersonalCientificoSerializer
    http_method_names = ['get', 'post','put', 'head', 'options']
  
    def get_queryset(self):
        return PersonalCientifico.objects.all()

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

class AsignacionResponsableRTViewSet(viewsets.ModelViewSet):
    """
    Vista para agregar un Llamada.
    """
    serializer_class = AsignacionResponsableSerializer
    http_method_names = ['get', 'post','put', 'head', 'options']
  
    def get_queryset(self):
        return AsignacionResponsableTecnicoRT.objects.all()

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