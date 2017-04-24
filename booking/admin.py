# coding=utf-8
from __future__ import unicode_literals

from .models import BookingHouse, BookingPerson,BookingRoom,Booking, RoomPhoto, Employee
from django.contrib import admin


class BookingHouseAdmin(admin.ModelAdmin):
    list_display = ('house_type', 'name', 'street', 'street_nr', 'city', 'city_code')
    class Meta:
        fields = ()


class BookingRoomPhotosInline(admin.StackedInline):
    model = RoomPhoto
class BookingRoomAdmin(admin.ModelAdmin):
    inlines = (BookingRoomPhotosInline,)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('choose_booking', 'booking_room','booking_person','status', 'payment_status', 'reservation_date',
                    'date_from', 'date_to', 'overall_price')

admin.site.register(BookingHouse,BookingHouseAdmin)
admin.site.register(BookingPerson)
admin.site.register(Employee)
admin.site.register(BookingRoom, BookingRoomAdmin)
admin.site.register(Booking,BookingAdmin)

