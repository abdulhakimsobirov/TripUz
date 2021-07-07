from django.db import models


from user.models import *
# from mapbox_location_field.models import AddressAutoHiddenField, LocationField  

import geocoder


class Province(models.Model):
    province = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.province

class District(models.Model):
    district = models.CharField(max_length=100, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.district + "(" + self.province.province + ")"

token = "pk.eyJ1Ijoic2NvdGhpcyIsImEiOiJjaWp1Y2ltYmUwMDBicmJrdDQ4ZDBkaGN4In0.sbihZCZJ56-fsFNKHXF8YQ"

class Station(models.Model):
    address = models.TextField(max_length=200, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=token)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Station, self).save(*args, **kwargs)

    


class Trip(models.Model):
    driver = models.OneToOneField(Driver, blank=True, on_delete=models.CASCADE)
    departure = models.ForeignKey(District, blank=True, related_name="from_where", on_delete=models.CASCADE)
    arrival = models.ForeignKey(District, blank=True, related_name="to_where", on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, blank=True, on_delete=models.CASCADE)
    datatime = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)
    seats = models.IntegerField(null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.departure.district + " - " + self.arrival.district

class OrderTrip(models.Model):
    trip = models.ForeignKey(Trip, blank=True, on_delete=models.CASCADE)
    passengers_phone = models.CharField(max_length=14, null=True)
    passengers_name = models.CharField(max_length=100, null=True)
    payment = models.BooleanField(default=False)

    def __str__(self):
        return self.passengers_name

