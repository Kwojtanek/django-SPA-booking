from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Booking, BookingRoom, BookingPerson, RoomPhoto, BookingHouse, BookingRoomAdditional, Employee


class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RoomPhoto


class RoomAdditionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BookingRoomAdditional


class BookingRoomSerializer(serializers.ModelSerializer):
    room_photos = RoomPhotoSerializer(
        many=True,
        read_only=True
    )
    dodatkowo = RoomAdditionSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = BookingRoom


class BookingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BookingPerson


class BookingSerializer(serializers.ModelSerializer):
    booking_room = serializers.StringRelatedField()
    booking_person = serializers.StringRelatedField()
    days_count = serializers.ReadOnlyField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Booking


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = get_user_model()

class BookingHouseSerializer(serializers.ModelSerializer):
    pracownicy = EmployeeSerializer(many=True, read_only=True)
    pokoje = BookingRoomSerializer(many=True, read_only=True)
    rezerwacje = BookingSerializer(many=True, read_only=True)
    rezerwujacy = BookingPersonSerializer(many=True, read_only=True)

    class Meta:
        model = BookingHouse
        fields = '__all__'
