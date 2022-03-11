from django.shortcuts import render
from .serializers import *
from credit.models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import *
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication, permissions



class CreditViewSet(ModelViewSet):
    serializer_class = CreditSerialiser
    queryset = Credit.objects.all()
    ordering_fields = ['update',]
    authentication_classes = [authentication.TokenAuthentication]
    


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    authentication_classes = [authentication.TokenAuthentication]