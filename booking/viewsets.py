from rest_framework import viewsets
from rest_framework.response import Response

from .models import BookingPerson
from .serializers import BookingPersonDetailSerializer
from django.shortcuts import get_object_or_404


class BookingPersonViewSet(viewsets.ViewSet):

    def retrieve(self, request,pk):
        queryset = BookingPerson.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BookingPersonDetailSerializer(user)
        return Response(serializer.data)

    def list(self,request):
        queryset = BookingPerson.objects.all()
        serializer = BookingPersonDetailSerializer(queryset,many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        pass
