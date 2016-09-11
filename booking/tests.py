# coding=utf-8
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
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

class AvailabilityTestCase(TestCase):
    """
    Class tests availability Manager returns
    """
    def setUp(self):
        BookingPerson.objects.create(email='Jacie@gmail.com',password='qwe123rtY')
        BookingPerson.objects.create(email='Gacie@gmail.com', password='qwe123rtY')

        BookingRoom.objects.create(name='Pokój', price=45)
        BookingRoom.objects.create(name='Apartament', price=100)

        # Booking.objects.create(additional_info='t1',
        #                        booking_person=BookingPerson.objects.get(pk=1),
        #                        booking_room=BookingRoom.objects.get(pk=1),
        #                        date_from=timezone.now().date() - timezone.timedelta(1),
        #                        date_to=timezone.now().date()  + timezone.timedelta(12))
        # Booking.objects.create(additional_info='t2',
        #                        booking_person=BookingPerson.objects.get(pk=1),
        #                        booking_room=BookingRoom.objects.get(pk=2),
        #                        date_from=timezone.now().date(),
        #                        date_to=timezone.now().date()  + timezone.timedelta(12))
        # Booking.objects.create(additional_info='t3',
        #                        booking_person=BookingPerson.objects.get(pk=1),
        #                        booking_room=BookingRoom.objects.get(pk=1),
        #                        date_from=timezone.now().date() + timezone.timedelta(12),
        #                        date_to=timezone.now().date() + datetime.timedelta(13))
        #
        # Booking.objects.create(additional_info='t4',
        #                        booking_person=BookingPerson.objects.get(pk=1),
        #                        booking_room=BookingRoom.objects.get(pk=1),
        #                        date_from=timezone.now().date() - timezone.timedelta(12),
        #                        date_to=timezone.now().date() + timezone.timedelta(12))
        # Booking.objects.create(additional_info='t5',
        #                        booking_person=BookingPerson.objects.get(pk=1),
        #                        booking_room=BookingRoom.objects.get(pk=2),
        #                        date_from=timezone.now().date(),
        #                        date_to=timezone.now().date()  + timezone.timedelta(12))
        # Booking.objects.create(additional_info='t6',
        #                        booking_person=BookingPerson.objects.get(pk=1),
        #                        booking_room=BookingRoom.objects.get(pk=1),
        #                        date_from=timezone.now().date() + timezone.timedelta(12),
        #                        date_to=timezone.now().date() + datetime.timedelta(13))
    def test_instance(self):
        #Test cases for is_colliding function:
        #   -Theres no entries in db so :returns Empty query
        #   -There is the same date reservation but different room :returns Empty Query
        #   -There is booked room within range booking is trying to proceed
        #   -There is different date same room :returns Empty Query
        #   -There is booked room but starts with day booking ends :returns Empty Query
        #   -There is booked room but ends with day booking starts :returns Empty Query
        #   -Booking was changed and starts to collide with other
        B1 = Booking(additional_info='t1',
                                booking_person=BookingPerson.objects.get(pk=1),
                                booking_room=BookingRoom.objects.get(pk=1),
                                date_from=timezone.now().date() + timezone.timedelta(1),
                                date_to=timezone.now().date()  + timezone.timedelta(12))
        self.assertFalse(B1.is_colliding())
        B1.save()
        B2 = Booking(additional_info='t2',
                               booking_person=BookingPerson.objects.get(pk=1),
                               booking_room=BookingRoom.objects.get(pk=2),
                               date_from=timezone.now().date(),
                               date_to=timezone.now().date()  + timezone.timedelta(12))
        self.assertFalse(B2.is_colliding())
        B2.save()
        self.assertFalse(B2.is_colliding())
        B3 = Booking(additional_info='t3',
                               booking_person=BookingPerson.objects.get(pk=1),
                               booking_room=BookingRoom.objects.get(pk=1),
                               date_from=timezone.now().date() + timezone.timedelta(5),
                               date_to=timezone.now().date() + timezone.timedelta(13))
        self.assertTrue(B3.is_colliding())
        B4 = Booking(additional_info='t4',
                               booking_person=BookingPerson.objects.get(pk=1),
                               booking_room=BookingRoom.objects.get(pk=1),
                               date_from=timezone.now().date() + timezone.timedelta(13),
                               date_to=timezone.now().date() + timezone.timedelta(14))
        self.assertFalse(B4.is_colliding())
        B4.save()
        B5 = Booking(additional_info='t5',
                               booking_person=BookingPerson.objects.get(pk=1),
                               booking_room=BookingRoom.objects.get(pk=1),
                               date_from=timezone.now().date(),
                               date_to=timezone.now().date()  + timezone.timedelta(13))
        self.assertTrue(B5.is_colliding())
        B6 = Booking(additional_info='t6',
                     booking_person=BookingPerson.objects.get(pk=1),
                     booking_room=BookingRoom.objects.get(pk=1),
                     date_from=timezone.now().date() + timezone.timedelta(14),
                     date_to=timezone.now().date() + timezone.timedelta(15))
        self.assertFalse(B6.is_colliding())
        self.assertEqual(B6.days_count(),1)
        B6.save()
