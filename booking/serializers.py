from rest_framework import serializers
from .models import Booking, BookingRoom, BookingPerson, HousePhoto, RoomPhoto

class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto

class BookingRoomSerializer(serializers.ModelSerializer):
    room_photos = RoomPhotoSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = BookingRoom


class BookingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingPerson


class BookingSerializer(serializers.ModelSerializer):
    booking_room = serializers.StringRelatedField()
    booking_person = serializers.StringRelatedField()
    days_count = serializers.ReadOnlyField(read_only=True)
    class Meta:
        model = Booking

class BookingPersonDetailSerializer(serializers.ModelSerializer):
    booking_person = BookingSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = Booking