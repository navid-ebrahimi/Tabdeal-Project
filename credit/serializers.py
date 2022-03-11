from rest_framework import serializers
from django.contrib.auth.models import User
from credit.models import *



class CreditSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = "__all__"

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"