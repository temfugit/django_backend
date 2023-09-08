from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from . import views
from django.views.generic import RedirectView

app_name = 'restaurant'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
    path('message/', views.msg),
]

