# coding=utf-8
from __future__ import unicode_literals
from .models import BookingHouse, BookingPerson
from django.contrib import admin
# Register your models here.
class BookingHouseAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(BookingHouse,BookingHouseAdmin)
admin.site.register(BookingPerson)