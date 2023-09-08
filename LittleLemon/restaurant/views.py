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
from rest_framework.decorators import api_view, permission_classes
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer


def index(request):
    return render(request, 'index.html', {})


class UserViewSet(viewsets.ModelViewSet):  
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    

@authentication_classes([TokenAuthentication])
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 



@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})
