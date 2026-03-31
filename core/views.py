from django.shortcuts import render
from .models import Event, PartnerPhoto

def partners_view(request):
    all_media = PartnerPhoto.objects.all()
    category_order = [choice[0] for choice in PartnerPhoto.PARTNER_CHOICES]
    sorted_media = sorted(
        all_media, 
        key=lambda x: category_order.index(x.partner_slug) if x.partner_slug in category_order else 999
    )

    return render(request, 'partners.html', {'photos': sorted_media})

def index(request):
    return render(request, 'index.html')

def events(request):
    events_list = Event.objects.all().order_by('date')
    return render(request, 'events.html', {'events': events_list})

def about(request):
    return render(request, 'about.html')
