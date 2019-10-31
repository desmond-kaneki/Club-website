from django.shortcuts import render

# Create your views here.

def past(request):
    return render(request, 'events/past.html')

def present(request):
    return render(request, 'events/present.html')

def future(request):
    return render(request, 'events/future.html')
