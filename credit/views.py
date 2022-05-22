from django.shortcuts import render
from .serializers import *
from credit.models import *
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import generics
from django.db import transaction



# class CreditViewSet(ModelViewSet):
#     serializer_class = CreditSerialiser
#     queryset = Credit.objects.all()
#     ordering_fields = ['update',]
#     authentication_classes = [authentication.TokenAuthentication]


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerialiser
#     authentication_classes = [authentication.TokenAuthentication]


class GetValue(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = CreditSerialiser
    queryset = Credit.objects.all()

    def get(self, request, pk):
        return self.retrieve(request, pk)


class ChargeCredit(generics.GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = CreditSerialiser
    queryset = Credit.objects.all()
    def post(self, request, pk):
        charge_amount = int(request.POST['value'])
        with transaction.atomic():
            current_credit = get_object_or_404(Credit.objects.select_for_update(), id=pk)
            current_credit.new_charge(charge_amount)
        return Response({'value': current_credit.value})


class Buy(generics.GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = CreditSerialiser
    queryset = Credit.objects.all()

    def post(self, request, pk):
        buy_cash = int(request.POST['value'])
        with transaction.atomic():
            current_credit = get_object_or_404(Credit.objects.select_for_update(), id=pk)
            current_credit.new_buy(buy_cash)
        return Response({'value': current_credit.value})