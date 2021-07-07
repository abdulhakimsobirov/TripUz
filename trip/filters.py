from django.db.models import fields
import django_filters

from .models import *

class TripFilter(django_filters.FilterSet):
    class Meta:
        model = Trip
        fields = ['departure', 'arrival']