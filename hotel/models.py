from datetime import datetime

import image as image
from django.db import models
from django.conf import settings

'''
class Guest(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name=models.CharField(max_length=100, null=True)

    def __str__(self):
         return self.name'''


class Category(models.Model):
    name=models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to ='images/category', null=True, blank=True)

    def __str__(self):
         return self.name

class Gallery (models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    def __str__(self):
         return self.image.url

class Room(models.Model):
     name = models.CharField(max_length=200, null=True)
     room_number = models.PositiveIntegerField()
     price = models.FloatField()
     short_desc=models.CharField(max_length=200, null=True)
     long_desc=models.TextField()
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     image = models.ImageField(upload_to='images/room', null=True, blank=True)
     gallery = models.ManyToManyField(Gallery, blank=True,related_name="product_img")
     booked=models.BooleanField(default=False)
     type = models.CharField(max_length=100)
     capacity =  models.IntegerField()
     beds =  models.IntegerField()

     def __str__(self):
         return self.name


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    #booking_address = models.ForeignKey(BookingInformation, on_delete=models.CASCADE)
    complete=models.BooleanField(default=False)
    Name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address_type = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=14, null=True)
    starttime = models.DateTimeField(default=datetime.now())
    endtime = models.DateTimeField(default=datetime.now())


    def __str__(self):
        return self.user.username