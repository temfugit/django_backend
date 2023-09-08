from django.shortcuts import render
from django.core import serializers
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status
from .models import BookingTable, MenuTable
from .serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db import models
from datetime import datetime
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from rest_framework import viewsets 


def index(request):
    return render(request, 'index.html', {})


class UserViewSet(viewsets.ModelViewSet):  
    queryset = User.objects.all()
    serializer_class = UserSerializer

