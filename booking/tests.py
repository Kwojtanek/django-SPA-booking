# coding=utf-8
from __future__ import unicode_literals
from django.test import TestCase
from .models import BookingHouse
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
    pass