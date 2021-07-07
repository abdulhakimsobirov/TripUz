from user import views
from django.urls import path
from . import views


urlpatterns = [
    path('trip_driver/', views.TripDriver.as_view(), name="trip_driver"),
    path('ordertrip/', views.orderTrip, name="ordertrip"),
]
