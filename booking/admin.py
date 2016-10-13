# coding=utf-8
from __future__ import unicode_literals

from django.forms import RadioSelect
from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import BookingHouse, BookingPerson,BookingRoom,Booking, HousePhoto, RoomPhoto
from django.contrib import admin

class HousePhotoInline(admin.StackedInline):
    model = HousePhoto

class BookingHouseAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    inlines = (HousePhotoInline,)
class BookingRoomPhotosInline(admin.StackedInline):
    model = RoomPhoto
class BookingRoomAdmin(admin.ModelAdmin):
    inlines = (BookingRoomPhotosInline,)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_room','booking_person','status', 'payment_status', 'reservation_date',
                    'date_from', 'date_to', 'overall_price')
admin.site.register(BookingHouse,BookingHouseAdmin)
admin.site.register(BookingPerson)
admin.site.register(BookingRoom, BookingRoomAdmin)
admin.site.register(Booking,BookingAdmin)
