from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers


app_name = "credit"
urlpatterns = [
    path('getvalue/<int:pk>/', GetValue.as_view(), name="getvalue"),
    path('chargecredit/<int:pk>/', ChargeCredit.as_view(), name="chargecredit"),
    path('buy/<int:pk>/', Buy.as_view(), name="buy"),
]
