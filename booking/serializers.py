from rest_framework import serializers
from .models import Booking, BookingRoom, BookingPerson


class BookingSerializer(serializers.ModelSerializer):
    days_count = serializers.ReadOnlyField(
        read_only=True
    )

    is_colliding = serializers.ReadOnlyField(
        read_only=True
    )
    class Meta:
        model = Booking