from django.urls import path
import app.views

urlpatterns = [
    path('concert_list', app.views.concerts_view, name='concert_list')
]
