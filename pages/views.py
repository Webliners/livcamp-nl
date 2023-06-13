from django.shortcuts import render
#from django.views.generic import TemplateView, View
from .models import Page

# Create your views here.

def base_view(request):
    return render(request, 'base.html')

def app_view(request):
    return render(request, 'app.html')

def camperverzekering_view(request):
    return render(request, 'camperverzekering.html')

def offerteaanvragen_view(request):
    return render(request, 'offerteaanvragen.html')

def zekerheidspakket_view(request):
    return render(request, 'zekerheidspakket.html')

def contact_view(request):
    return render(request, 'contact.html')

def reisdagboek_view(request):
    return render(request, 'reisdagboek.html')

def overlivcamp_view(request):
    return render(request, 'overlivcamp.html')

def lidmaatschap_view(request):
    return render(request, 'lidmaatschap.html')

def privacypolicy_view(request):
    return render(request, 'privacypolicy.html')

def algemenevoorwaarden_view(request):
    return render(request, 'algemenevoorwaarden.html')

def partners_view(request):
    return render(request, 'partners.html')

def camperreizen_view(request):
    return render(request, 'camperreizen.html')

def campershop_view(request):
    return render(request, 'campershop.html')

def camperroute_view(request):
    return render(request, 'camperroute.html')

def voorbedrijven_view(request):
    return render(request, 'voorbedrijven.html')

def voorcamperplaatsen_view(request):
    return render(request, 'voorcamperplaatsen.html')

def campertraining_view(request):
    return render(request, 'campertraining.html')

def vacatures_view(request):
    return render(request, 'vacatures.html')

def reisadvies_view(request):
    return render(request, 'reisadvies.html')

def reisadviesaanvragen_view(request):
    return render(request, 'reisadviesaanvragen.html')






