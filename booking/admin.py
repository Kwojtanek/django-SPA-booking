# coding=utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from .models import BookingHouse, BookingPerson,BookingRoom,Booking
from django.contrib import admin


class BookingHouseAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(BookingHouse,BookingHouseAdmin)
admin.site.register(BookingPerson)
admin.site.register(BookingRoom)
admin.site.register(Booking)