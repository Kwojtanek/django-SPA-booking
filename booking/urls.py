from __future__ import unicode_literals
from django.conf.urls import url, include
from rest_framework import generics
from rest_framework import routers

from .models import Booking, BookingRoom
from .serializers import BookingSerializer, BookingRoomSerializer
from .viewsets import BookingPersonViewSet

router = routers.SimpleRouter()
router.register(r'booking-person', BookingPersonViewSet, base_name='booking-person')

urlpatterns = [
    url(r'^api/booking/$', generics.ListAPIView.as_view(queryset=Booking.objects.all(),
                                                        serializer_class=BookingSerializer),
                                                        name='booking-list'),
    url(r'api/booking-room/$', generics.ListAPIView.as_view(queryset=BookingRoom.objects.all(),
                                                            serializer_class=BookingRoomSerializer),
                                                            name='booking-room-list'),
    url(r'^api/', include(router.urls, namespace='api')),
]
