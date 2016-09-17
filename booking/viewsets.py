from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import BookingPerson
from .serializers import BookingPersonDetailSerializer, BookingPersonSerializer
from django.shortcuts import get_object_or_404


class BookingPersonViewSet(viewsets.ViewSet):
    """
    Class provides api about person making booking:
    It should contain:
        -list of all Persons. Permision only employees and admin (GET)
        -Single person information. Should display all information about reservation make by person Permissions: making reservation person, employee and admin, (GET)
        -also update(PUT), delete(DELETE), create(POST) (CRUD) person Permissions: making reservation person, employee and admin

    """
    def list(self,request):
        queryset = BookingPerson.objects.all()
        serializer = BookingPersonSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk):
        queryset = BookingPerson.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BookingPersonDetailSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            Bp = BookingPerson.objects.get(pk=pk)
            Bp.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def create(self,request):
        serializer = BookingPersonSerializer(BookingPerson(), request.data)
        if serializer.is_valid():
            B = BookingPerson(**request.data)
            B.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def update(self,request,pk):
        pass