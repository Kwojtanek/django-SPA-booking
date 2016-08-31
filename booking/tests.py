# coding=utf-8
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import BookingHouse, BookingPerson, BookingRoom, Booking
import datetime
# Create your tests here.


class BookingHouseTestCase(TestCase):
    longMessage = True
    def setUp(self):
        BookingHouse.objects.create(house_type='Hotel',
                              name='Hata',
                              street='Rzemieślnicza',
                              street_nr=1,
                              city='Wągrzce',
                              additional_info='Brak ścian',
                                    email='bla@gmail.com')

    def test_singleton(self):
        Hata = BookingHouse.objects.get(name='Hata')
        self.assertEqual(Hata.pk, 1)

class BookingPersonTestCase(TestCase):
    #Simple test if user can be created
    def setUp(self):
        BookingPerson.objects.create(email='Jacie@gmail.com',password='qwe123rtY')

    def test_instance(self):
        Ja = BookingPerson.objects.last()
        self.assertEqual(Ja.email,'Jacie@gmail.com')

class BookingRoomTestCase(TestCase):
    def setUp(self):
        BookingRoom.objects.create(name='Pokój')

    def test_instance(self):
        pokoj = BookingRoom.objects.get(name='Pokój')
        self.assertEqual(pokoj.pk,1)

class BookingTestCase(TestCase):
    def setUp(self):
        BookingPerson.objects.create(email='Jacie@gmail.com',password='qwe123rtY')
        BookingPerson.objects.create(email='Gacie@gmail.com', password='qwe123rtY')

        BookingRoom.objects.create(name='Pokój', price=45)
        BookingRoom.objects.create(name='Apartament', price=100)

        Booking.objects.create(booking_person=BookingPerson.objects.get(pk=1),booking_room=BookingRoom.objects.get(pk=1),
                           date_from=datetime.date(2015,8,31), date_to=datetime.date(2015,8,31))
        Booking.objects.create(booking_person=BookingPerson.objects.get(pk=1),booking_room=BookingRoom.objects.get(pk=1),
                           date_from=datetime.date(2015,9,1), date_to=datetime.date(2015,9,3))
    def test_instance(self):
        Person1 = BookingPerson.objects.get(email='Jacie@gmail.com')
        Person2 = BookingPerson.objects.get(email='Gacie@gmail.com')
        Room1 = BookingRoom.objects.get(name='Pokój')
        Room2 = BookingRoom.objects.get(name='Apartament')
        Booking1 = Booking.objects.get(pk=1)
        Booking2 = Booking.objects.get(pk=2)

        self.assertRaises(ValidationError,lambda :Booking1.clean())
        self.assertEqual(Booking2.days_count(),2)
        self.assertEqual(Booking2.overall_price,90)

    def test_availablity(self):
        pass