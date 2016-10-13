# coding=utf-8
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, User
from django.utils import timezone
from django.core.mail import send_mail


class BookingHouse(models.Model):
    """
    Singleton object that keeps information about Hotel, or other residential pension
    """
    house_choices = (('Pensjonat', 'Pensjonat'), ('Kemping', 'Kemping'),
                     ('Pole biwakowe', 'Pole biwakowe'), ('Dom wycieczkowy', 'Dom wycieczkowy'),
                     ('Hotel', 'Hotel'), ('Motel', 'Motel'), ('Schronisko', 'Schronisko'),
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
    city_code = models.CharField(max_length=16, verbose_name=_('Kod pocztowy'), blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=16,verbose_name=_('Numer telefonu'), blank=True)
    infos = models.TextField(blank=True, verbose_name=_('Opis obiektu'))
    additional_info = models.TextField(blank=True, verbose_name=_('Dodatkowe informacje'))

    def save(self, *args, **kwargs):
        self.pk = 1
        return super(BookingHouse, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s %s' % (self.house_type, self.name)

    def __str__(self):
        return '%s %s' % (self.house_type, self.name)

    class Meta:
        verbose_name_plural = "Twój obiekt"
        verbose_name = verbose_name_plural


class BookingPerson(AbstractBaseUser):
    """
    Model contains information about person making booking
    """

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    forename = models.CharField(max_length=32, blank=True, verbose_name=_('Imię'))
    surname = models.CharField(max_length=64, blank=True, verbose_name=_('Nazwisko'))

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

    identification_number = models.CharField(max_length=32, blank=True, verbose_name=_('Nr. dowodu/PESEL'))
    additional_info = models.TextField(blank=True, verbose_name=_('Dodatkowe informacje'))
    date_joined = models.DateTimeField(_('Data utworzenia'), default=timezone.now)

    is_active = models.BooleanField(
        _('Aktywny'),
        default=True,
        help_text=_(
            'Wyznacza czy użytkownik jest aktywny. Zmień tę wartość zamiast usuwać użytkownika.'
        ),
    )

    is_confirmed = models.BooleanField(
        _('Potwierdzony email'),
        default=False,
        help_text=_('Potwierdzona rejestracja mailowa')
    )

    objects = UserManager()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.forename, self.surname)
        return full_name.strip()

    def get_short_name(self):
        """"
        Returns the short name for the user.
        """
        return self.forename

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name_plural = _("Rezerwujący")
        verbose_name = verbose_name_plural


class BookingRoom(models.Model):
    """
    Model contains information about room that will be booked
    """

    name = models.CharField(max_length=64, default='Pokój', verbose_name=_('Nazwa pokoju'))
    level = models.PositiveIntegerField(verbose_name=_('Piętro'), null=True)
    size = models.CharField(verbose_name=_('Powierzchnia pokoju'), max_length=16, blank=True)
    bathroom = models.BooleanField(verbose_name=_('Prywatna łazienka'), default=True)
    television = models.BooleanField(verbose_name=_('Telewizor'), default=True)
    kitchen = models.BooleanField(verbose_name=_('Aneks kuchenny'), default=False)
    internet = models.BooleanField(verbose_name=_("WiFi/internet"), default=True)
    air_conditioning = models.BooleanField(verbose_name='Klimatyzacja',default=False)
    pets_allowed = models.BooleanField(verbose_name='Zwierzęta', default=False)
    bed = models.CharField(verbose_name=_('Łóżka'), max_length=64, blank=True)
    max_people = models.PositiveIntegerField(verbose_name=_('Maksymalna ilość osób'), null=True)
    price = models.PositiveIntegerField(verbose_name='Cena za jedną dobę', null=True)
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pokoje"
        verbose_name = "Pokój"


class AfterTodayManager(models.Manager):
    def get_queryset(self):
        return super(AfterTodayManager, self).get_queryset().filter(date_to__gte=timezone.now())


class Booking(models.Model):
    """
    Booking model should contain:
    Foreign key to user that will book room
    Foreign key to room that will be booked
    overall prize of booked room
    :date_from booked room
    :date_to booked room
    """
    booking_person = models.ForeignKey(BookingPerson, related_name='booking_person',
                                       verbose_name='Rezerwujący')
    booking_room = models.ForeignKey(BookingRoom, related_name='booking_room',
                                     verbose_name=_('Pokój'))
    reservation_date = models.DateTimeField(default=timezone.now, verbose_name=_('Data dokonania rezerwacji.'))
    date_from = models.DateField(verbose_name=_('Rezerwacja od'))
    date_to = models.DateField(verbose_name=_('Rezerwacja do'))
    additional_info = models.TextField(verbose_name='Dodatkowe informacje', null=True, blank=True)

    def days_count(self):
        return (self.date_to - self.date_from).days

    overall_price = models.PositiveIntegerField(verbose_name=_('Cena za cały pobyt'), blank=True, null=True)


    STATUS_CHOICE = (('w','Oczekuje na potwierdzenie'),
                     ('r','Potwierdzona rezerwacja'),
                     ('c','Skasowana'))

    status = models.CharField(max_length=4,choices=STATUS_CHOICE,
                              verbose_name=_('Status rezerwacji'),
                              default='w')
    payment_status = models.BooleanField(default=False, verbose_name='Status płatności')
    # --------------Managers-------------#
    objects = models.Manager()
    after_today = AfterTodayManager()

    def is_colliding(self):
        """
        :return: True or false if overlaps other date range
        Should it be in this logic?
        """
        # If Booking is not empty for this room
        # Excludes self from results coz' self cant collide with itself
        # Takes in count only dates after today
        if self.pk:
            booking = Booking.after_today.exclude(pk=self.pk)
        else:
            booking = Booking.after_today.all()
        booking = booking.filter(booking_room__id=self.booking_room.id)

        for b in booking:
            if b.date_from < self.date_to and self.date_from < b.date_to:
                return True
        return False

    def validate(self):
        try:
            if self.is_colliding():
                raise ValidationError('Data dla %s jest już zajęta' % self.booking_room.name)
            if self.days_count() <= 0:
                raise ValidationError('Data przyjazdu nie może być taka sama ani późniejsza niż data wyjazdu')
        except:
            raise SystemError('Coś poszło nie tak')

    def clean(self):
        self.validate()

    def save(self, *args, **kwargs):
        self.validate()

        # If no value for overall price is provided it will count it
        if self.overall_price is None:
            self.overall_price = self.booking_room.price * self.days_count()
        return super(Booking, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'rezerwujący %s, %s. od %s do %s' % (
            self.booking_person, self.booking_room, self.date_from, self.date_to)

    def __str__(self):
        return 'rezerwujący %s, %s. od %s do %s' % (
            self.booking_person, self.booking_room, self.date_from, self.date_to)

    class Meta:
        verbose_name_plural = "Rezerwacje"
        verbose_name = verbose_name_plural
        ordering = ('-reservation_date',)


class RoomPhoto(models.Model):
    room = models.ForeignKey(to=BookingRoom,related_name='room_photos',verbose_name='pokój')
    image = models.ImageField(upload_to='media/',verbose_name='Zdjęcie')

    def __unicode__(self):
        return self.room.name

    class Meta:
        verbose_name = 'Zdjęcie pokoju'
        verbose_name_plural = 'Zdjęcia pokoju'


class HousePhoto(models.Model):
    house = models.ForeignKey(to=BookingHouse, related_name='house_photos', verbose_name='Budynek')
    image = models.ImageField(upload_to='media/',verbose_name='Zdjęcie')

    def __unicode__(self):
        return self.house.name

    class Meta:
        verbose_name = 'Zdjęcie budynku'
        verbose_name_plural = 'Zdjęcia budynku'

class Employee(User):
    pass