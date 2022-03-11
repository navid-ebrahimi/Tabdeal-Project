from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers


app_name = "credit"

router = routers.SimpleRouter()
router.register('', CreditViewSet, basename="credit")
router.register('users', UserViewSet, basename="users")
urlpatterns = [
    path('', include(router.urls)),
]
