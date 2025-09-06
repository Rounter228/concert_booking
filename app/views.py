from django.shortcuts import render
from .models import Concert

def home(request):
    concerts = Concert.objects.all()
    return render(request, "home.html", {"concerts": concerts})
