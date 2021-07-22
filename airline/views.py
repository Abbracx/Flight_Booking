from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Flight, Airport, Passenger

def index(request):

    context = {
        "flights" : Flight.objects.all()
    }
    return render(request, "airline/index.html", context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        raise Http404('Flight Does not exist')
    ctx = {
        'flight': flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights__id=flight_id).all()
        }
    return render(request, 'airline/detail_flight.html', ctx)

def book(request, flight_id):
    try:
        passenger_id = request.POST['passenger']
        print(f'paseenger id is {passenger_id}')
        passenger = Passenger.objects.get(pk=passenger_id)
        print(f'paseenger is {passenger}')
        flight = Flight.objects.get(pk=flight_id)
        print(f'flight is {flight}')
    except KeyError:
        raise Http404('Invalid ID provided.')
    except Passenger.DoesNotExist:
        raise Http404('Passenger Does Not Exist.')
    except Flight.DoesNotExist:
        raise Http404('Flight Does Not Exist.')
    flight.passengers.add(passenger)
    # passenger.fligthts.add(flight)
    return redirect('airline:detail_flight', fligtht_id=flight.id)
    # return HttpResponseRedirect(reverse('airline:detail_flight', args=[flight.id]))
    # return HttpResponseRedirect(reverse('airline:detail_flight', args=(flight_id,)))
