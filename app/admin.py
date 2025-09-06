from django.contrib import admin
from .models import Performer, Hall, Seat, Concert, Ticket, Booking

admin.site.register(Performer)
admin.site.register(Hall)
admin.site.register(Seat)
admin.site.register(Concert)
admin.site.register(Ticket)
admin.site.register(Booking)
