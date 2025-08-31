from django.shortcuts import render
from .models import Concert, Ticket


def concerts_view(request):
    concerts = Concert.objects.all
    print(concerts)