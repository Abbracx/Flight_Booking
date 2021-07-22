from django.contrib import admin
from .models import Flight, Airport, Passenger

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['origin', 'destination']

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['first', 'last']
