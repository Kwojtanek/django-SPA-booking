# coding=utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.crypto import get_random_string

class BookingHouse(models.Model):
    """
    Singleton object that keeps information about Hotel, or other residential pension
    """
    house_choices = (('Pensjonat', 'Pensjonat'), ('Kemping', 'Kemping'),
                     ('Pole biwakowe', 'Pole biwakowe'), ('Dom wycieczkowy', 'Dom wycieczkowy'),
                     ('Hotel', 'Hotel'), ('Motel','Motel'), ('Schronisko', 'Schronisko'),
                     ('Inny obiekt', 'Inny obiekt'))

    house_type = models.CharField(blank=False,
                                  choices=house_choices,
                                  verbose_name=_('Rodzaj obiektu'),
                                  max_length=128
                                  )
    name = models.CharField(blank=False,
                            verbose_name=_('Nazwa obiektu'),
                            max_length=128)
    street = models.CharField(blank=False,
                              verbose_name=_('Ulica'),
                              max_length=128)
    street_nr = models.CharField(blank=False,
                                 verbose_name=_('Numer domu'),
                                 max_length=64)
    city = models.CharField(blank=False,
                            max_length=128,
                            verbose_name=_('Miejscowość'))
    city_code = models.CharField(max_length=16, verbose_name=_('Kod pocztowy'),blank=True)
    email = models.EmailField(blank=True)
    infos = models.TextField(blank=True,verbose_name=_('Opis obiektu'))
    additional_info = models.TextField(blank=True, verbose_name=_('Dodatkowe informacje'))

    def save(self, *args, **kwargs):
        self.pk = 1
        return super(BookingHouse,self).save(*args,**kwargs)


    def __unicode__(self):
        return '%s %s' % (self.house_type, self.name)

    def __str__(self):
        return '%s %s' % (self.house_type, self.name)

    class Meta:
        verbose_name_plural = "Twój obiekt"
        verbose_name = verbose_name_plural

class BookingPerson(AbstractBaseUser):
    """
    Model contains informations about person making booking
    """

    email = models.EmailField(unique=True)
    forname = models.CharField(max_length=32, blank=True,verbose_name=_('Imię'))
    last_name =models.CharField(max_length=64, blank=True,verbose_name=_('Nazwisko'))

    street = models.CharField(blank=True,
                              verbose_name=_('Ulica'),
                              max_length=128)
    street_nr = models.CharField(blank=True,
                                 verbose_name=_('Numer domu'),
                                 max_length=64)
    city = models.CharField(blank=True,
                            max_length=128,
                            verbose_name=_('Miejscowość'))
    city_code = models.CharField(max_length=16, blank=True, verbose_name=_('Kod pocztowy'))

    additional_info = models.TextField(blank=True,
                                       verbose_name=_('Dodatkowe informacje'))
    class Meta:
        verbose_name_plural = "Rezerwujący"
        verbose_name = verbose_name_plural

class BookingRoom(models.Model):
    level = models.PositiveIntegerField(verbose_name=_('piętro'), blank=True)
    size = models.CharField(verbose_name=_('Powierzchnia pokoju'), max_length=16,blank=True)
    bathroom = models.BooleanField(verbose_name=_('Prywatna łazienka'),default=True)
    television = models.BooleanField(verbose_name=_('Telewizor'), default=True)
    kitchen = models.BooleanField(verbose_name=_('Aneks kuchenny'), default=False)
    internet = models.BooleanField(verbose_name=_("WiFi/internet"), default=True)
    bed = models.CharField(verbose_name=_('Łóżka'),blank=True)
    max_people = models.PositiveIntegerField(verbose_name=_('Maksymalna ilość osób'), blank=True)
    price = models.PositiveIntegerField()


    """
    Model contains informations about room that will be booked
    """
    pass

# class Booking(models.Model):
#     pass