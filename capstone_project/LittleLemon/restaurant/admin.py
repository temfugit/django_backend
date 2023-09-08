from django.contrib import admin
from .models import MenuTable, BookingTable


# Register your models here.
admin.site.register(BookingTable)
admin.site.register(MenuTable)
