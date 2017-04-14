from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import BookingPerson
from .serializers import BookingPersonSerializer
from .permissions import BookingPersonPermission


class BookingPersonViewSet(ModelViewSet):
    """
    Class provides api about person making booking:
    It should contain:
        -list of all Persons. Permision only employees and admin (GET)
        -Single person information. Should display all information about reservation make by person Permissions: making reservation person, employee and admin, (GET)
        -also update(PUT), delete(DELETE), create(POST) (CRUD) person Permissions: making reservation person, employee and admin

    """
    queryset = BookingPerson.objects.all()
    serializer_class = BookingPersonSerializer
    permission_classes = (AllowAny,)