# coding=utf-8
from __future__ import unicode_literals, print_function

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APITestCase
from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import BookingPerson

class BookingPersonTests(APITestCase):
    def test_create_delete_person(self):
        """
        Ensure we can create a new account object.
        """
        data = {'email':'gacie@gmail.com','password':'12ade12edas213'}
        response = self.client.post('/api/booking-person/',data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BookingPerson.objects.count(),1)
        B = BookingPerson.objects.get(pk=1)
        self.assertEqual(B.email,'gacie@gmail.com')
        response = self.client.delete('/api/booking-person/%s' % B.pk, format='json')
        self.assertEqual(BookingPerson.objects.count(),0)