from django.db import models
from django.contrib.auth.models import User


class Performer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ім'я виконавця/групи")
    genre = models.CharField(max_length=100, blank=True, null=True, verbose_name="Жанр")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")

    def __str__(self):
        return self.name


class Hall(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва залу")
    address = models.CharField(max_length=255, verbose_name="Адреса")
    capacity = models.PositiveIntegerField(verbose_name="Вмістимість")

    def __str__(self):
        return f"{self.name} ({self.address})"


class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name="seats")
    row = models.CharField(max_length=5, verbose_name="Ряд")
    number = models.PositiveIntegerField(verbose_name="Номер місця")

    class Meta:
        unique_together = ("hall", "row", "number")

    def __str__(self):
        return f"Зал {self.hall.name} – Ряд {self.row}, Місце {self.number}"


class Concert(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва концерту")
    date = models.DateTimeField(verbose_name="Дата та час")
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE, related_name="concerts")
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name="concerts")

    def __str__(self):
        return f"{self.title} ({self.performer.name}) – {self.date.strftime('%d.%m.%Y %H:%M')}"


class Ticket(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, related_name="tickets")
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name="tickets")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    is_reserved = models.BooleanField(default=False, verbose_name="Заброньований")

    class Meta:
        unique_together = ("concert", "seat")

    def __str__(self):
        return f"{self.concert.title} | {self.seat}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name="booking")
    booked_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата бронювання")

    def __str__(self):
        return f"{self.user.username} забронював {self.ticket}"

