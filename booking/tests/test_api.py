# coding=utf-8
from __future__ import unicode_literals, print_function

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APITestCase
from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import BookingPerson

class BookingPersonTests(APITestCase):
    def setUp(self):
        data1 = {'email':'gacie123@gmail.com','password':'12ade12edas213'}
        data2 = {'email':'gacie1234@gmail.com','password':'12ade12edas213','is_confirmed': True}

        BookingPerson.objects.create(**data1)
        BookingPerson.objects.create(**data2)
    def test_create_delete_person(self):
        """
        Ensures we can create and delete new account object.
        """
        data = {'email':'gacie@gmail.com','password':'12ade12edas213'}
        response = self.client.post('/api/booking-person/',data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BookingPerson.objects.count(),3)
        B = BookingPerson.objects.get(pk=1)
        self.assertEqual(B.email,'gacie123@gmail.com')
        response = self.client.delete('/api/booking-person/%s/' % B.pk, format='json')
        self.assertEqual(BookingPerson.objects.count(),2)
