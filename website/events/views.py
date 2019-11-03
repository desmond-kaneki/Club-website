from django.shortcuts import render, get_object_or_404
from .models import Event
import datetime

# Create your views here.

def past(request):
    events = Event.objects
    return render(request, 'events/past.html', {'events':events})

def present(request):
    events = Event.objects
    for event in events.all() :
        d1 = datetime.date.today()
        d2 = event.event_date
        if d2>d1:
            event.event_time = 'f'
            event.save()
        elif d1>d2:
            event.event_time = 'p'
            event.save()
        else:
            event.event_time = 'n'
            event.save()
    return render(request, 'events/present.html', {'events':events})

def future(request):
    events = Event.objects
    return render(request, 'events/future.html', {'events':events})

def event(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    return render(request, 'events/detail.html', {'event':event})


