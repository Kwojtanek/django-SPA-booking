from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import BookingHouseSerializer
from .models import BookingHouse

class RetrieveBookingHouse(RetrieveAPIView):
    serializer_class = BookingHouseSerializer
    queryset = BookingHouse
    lookup_field = 'token'

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

