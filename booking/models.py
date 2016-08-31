# coding=utf-8
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
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
    Model contains informations about room that will be booked
    """
    name = models.CharField(max_length=64, default='Pokój', verbose_name=_('Nazwa pokoju'))
    level = models.PositiveIntegerField(verbose_name=_('Piętro'), null=True)
    size = models.CharField(verbose_name=_('Powierzchnia pokoju'), max_length=16, blank=True)
    bathroom = models.BooleanField(verbose_name=_('Prywatna łazienka'), default=True)
    television = models.BooleanField(verbose_name=_('Telewizor'), default=True)
    kitchen = models.BooleanField(verbose_name=_('Aneks kuchenny'), default=False)
    internet = models.BooleanField(verbose_name=_("WiFi/internet"), default=True)
    bed = models.CharField(verbose_name=_('Łóżka'), max_length=64, blank=True)
    max_people = models.PositiveIntegerField(verbose_name=_('Maksymalna ilość osób'), null=True)
    price = models.PositiveIntegerField(verbose_name='Cena za jedną dobę',null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pokoje"
        verbose_name = "Pokój"


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

    def days_count(self):
        return (self.date_to - self.date_from).days

    overall_price = models.PositiveIntegerField(verbose_name=_('Cena za cały pobyt'), blank=True, null=True)

    def is_available(self):
        """
        :return: Validation error if room is not available
        Should it be in this logic?
        """
        # If Booking is not empty
        # Check if it's made booking for this room
        # and date_from is not in range date_from to date_to
        # and date_to is not in range date_from to date_to
        booking = Booking.objects.all()
        if booking:
            availb_rooms = booking.filter(reservation_date__gte=timezone.now(),
                                          booking_room_id=self.booking_room_id,
                                          date_from__range=[self.date_from, self.date_to],
                                          date_to__range=[self.date_from, self.date_to])
            if availb_rooms:
                return True
        else:
            return True

    def clean(self):
        self.is_available()
        if self.days_count() <= 0:
            raise ValidationError('Data przyjazdu nie może być taka sama ani późniejsza niż data wyjazdu')

    def save(self, *args, **kwargs):
        # If no value for overall price is provided it will count it
        if self.overall_price is None:
            self.overall_price = self.booking_room.price * self.days_count()
        return super(Booking, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'rezerwujący %s, %s. od %s do %s' % (self.booking_person, self.booking_room,
                                                    self.date_from, self.date_to)

    def __str__(self):
        return 'rezerwujący %s, %s. od %s do %s' % (self.booking_person, self.booking_room,
                                                    self.date_from, self.date_to)

    class Meta:
        verbose_name_plural = "Rezerwacje"
        verbose_name = verbose_name_plural
        ordering = ('-reservation_date',)
