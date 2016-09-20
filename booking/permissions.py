from rest_framework import permissions


class BookingPersonPermission(permissions.BasePermission):
    """
    Booking person can:
        -CRUD Booking object?

    """