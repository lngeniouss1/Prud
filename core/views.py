from django.shortcuts import render
from .models import Event, PartnerPhoto

def partners_view(request):
    photos = PartnerPhoto.objects.all().order_by('-uploaded_at')
    return render(request, 'partners.html', {'photos': photos})

def index(request):
    return render(request, 'index.html')

def events(request):
    events_list = Event.objects.all().order_by('date')
    return render(request, 'events.html', {'events': events_list})

def about(request):
    return render(request, 'about.html')
