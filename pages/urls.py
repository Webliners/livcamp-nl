from django.urls import path
from . import views
#from .views import AlgemeneVoorwaardenView

urlpatterns = [
    path('', views.base_view, name='base'),
    path('app/', views.app_view, name='app'),
    path('camperverzekering/', views.camperverzekering_view, name='camperverzekering'),
    path('offerte-aanvragen/', views.offerteaanvragen_view, name="offerte"),
    path('camper-zekerheidspakket/', views.zekerheidspakket_view, name='zekerheidspakket'),
    path('camper-reisdagboek/', views.reisdagboek_view, name='reisdagboek'),
    path('contact/', views.contact_view, name='contact'),
    path('over-livcamp/', views.overlivcamp_view, name='overlivcamp'),
    path('lidmaatschap/', views.lidmaatschap_view, name='lidmaatschap'),
    path('privacy-policy/', views.privacypolicy_view, name="privacypolicy"),
    #path('algemene-voorwaarden/', AlgemeneVoorwaardenView.as_view(), name='algemenevoorwaarden'),
    path('algemene-voorwaarden/', views.algemenevoorwaarden_view, name='algemenevoorwaarden'),
    path('partners/', views.partners_view, name='partners'),
    path('camperreizen/', views.camperreizen_view, name='camperreizen'),
    path('campershop/', views.campershop_view, name='campershop'),
    path('camperroute/', views.camperroute_view, name='camperroute'),
    path('voor-bedrijven/', views.voorbedrijven_view, name='voorbedrijven'),
    path('voor-camperplaatsen/', views.voorcamperplaatsen_view, name='voorcamperplaatsen'),
    path('campertraining/', views.campertraining_view, name='campertraining'),
    path('vacatures/', views.vacatures_view, name='vacatures'),
    path('camper-reisadvies/', views.reisadvies_view, name='reisadvies'),
    path('reisadvies-aanvragen/', views.reisadviesaanvragen_view, name='reisadviesaanvragen'),
]