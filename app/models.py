from django.db import models
from django.contrib.auth.models import User


class Concert(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва концерту")
    date = models.DateTimeField(verbose_name="Дата проведення")
    location = models.CharField(max_length=255, verbose_name="Місце проведення")
    total_tickets = models.PositiveIntegerField(verbose_name="Загальна кількість квитків")


class Ticket(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, related_name="tickets")
    seat_number = models.CharField(max_length=10, verbose_name="Номер місця")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    is_available = models.BooleanField(default=True, verbose_name="Доступний")


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="bookings")
    booking_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата бронювання")