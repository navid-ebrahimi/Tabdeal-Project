from django.test import TestCase
from credit.models import *
from ..serializers import *
from credit.models import *
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework import status
from django.db import transaction
from rest_framework import authentication, permissions


class CreditTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="hamid", password="hamid")
        credit1 = Credit.objects.create(account_owner=self.user, value = 30)

        self.user = User.objects.create_user(username="navid", password="1234")
        credit2 = Credit.objects.create(account_owner=self.user, value = 30)

        self.user = User.objects.create_user(username="omid", password="1234")
        credit3 = Credit.objects.create(account_owner=self.user, value = 30)

        credit2.new_charge(40)
        credit3.new_buy(10)
        # current_credit.new_charge(30)

    def test_Check_Credit_Value(self):
        wallet = Credit.objects.get(id = 1)
        self.assertEqual(wallet.value,30)

    def test_Check_Charge(self):
        wallet = Credit.objects.get(id = 2)
        self.assertEqual(wallet.value,70)

    def test_Check_Buy(self):
        wallet = Credit.objects.get(id = 3)
        self.assertEqual(wallet.value,20)
