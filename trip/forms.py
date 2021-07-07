from django.forms import fields
from user import models
import django


from django.forms.models import ModelForm
from django import forms
from .models import *


class ProvinceForm(ModelForm):
    class Meta:
        model = Province
        fields = "__all__"


class DistrictForm(ModelForm):
    class Meta:
        model = District
        fields = "__all__"

class StationForm(ModelForm):
    class Meta:
        model = Station
        fields = "__all__"


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = "__all__"


class OrderTripForm(ModelForm):
    class Meta:
        model = OrderTrip
        fields = "__all__"

