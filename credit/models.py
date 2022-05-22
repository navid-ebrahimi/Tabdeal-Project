from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from rest_framework.response import Response
from rest_framework import status


class navid(models.Model):
    owner = models.CharField(max_length=255)
    value = models.IntegerField()


class Credit(models.Model):
    account_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def new_charge(self, amount):
        self.value += amount
        self.save()
        new_charge = Charge.objects.create(wallet=self, amount=amount)
        return new_charge.save()

    def new_buy(self, amount):
        if self.value < amount:
            # raise ValueError(status.HTTP_400_BAD_REQUEST)
            return status.HTTP_400_BAD_REQUEST
        self.value -= amount
        self.save()
        new_buy = Buy.objects.create(wallet=self, amount=amount)
        return new_buy.save()

    def __str__(self):
        return f'{self.account_owner}'


class Buy(models.Model):
    wallet = models.ForeignKey(Credit, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    amount = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return f'{self.wallet.account_owner}: {self.amount}'


class Charge(models.Model):
    wallet = models.ForeignKey(Credit, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    amount = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return f'{self.wallet.account_owner}: {self.amount}'