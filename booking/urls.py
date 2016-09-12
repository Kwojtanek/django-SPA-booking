from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib import admin
from rest_framework import generics

from .models import Booking, BookingRoom, BookingPerson
from .serializers import BookingSerializer, BookingRoomSerializer, BookingPersonSerializer

urlpatterns = [
    url(r'^api/booking/$', generics.ListAPIView.as_view(queryset=Booking.objects.all(), serializer_class=BookingSerializer), name='booking-list'),
    url(r'api/booking-room/$', generics.ListAPIView.as_view(queryset=BookingRoom.objects.all(), serializer_class=BookingRoomSerializer), name='booking-room-list'),
    url(r'api/booking-person/$', generics.ListAPIView.as_view(queryset=BookingPerson.objects.all(), serializer_class=BookingPersonSerializer), name='booking-person-serializer')
]
