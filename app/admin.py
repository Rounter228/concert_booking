from django.contrib import admin
from .models import *


admin.site.register(Concert)
admin.site.register(Ticket)
admin.site.register(Booking)