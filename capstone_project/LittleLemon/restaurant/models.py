from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class BookingTable(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateField(db_index=True)
    