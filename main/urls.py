from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('clients/', views.clients, name='clients'),
    path('values/', views.values, name='values'),
    path('licenses/', views.licenses, name='licenses'),
    path('about2/', views.about2, name='about2'),

    # Projects URLs
    path('projects/', views.projects, name='projects'),
    path('projects/water-supply-system/', views.water_supply_system, name='water_supply_system'),
    path('projects/air-conditioner-installation/', views.air_conditioner_installation, name='air_conditioner_installation'),
    path('projects/rehabilitation-project/', views.rehabilitation_project, name='rehabilitation_project'),
    path('projects/hvac-system-installation/', views.installation_of_hvac_system, name='installation_of_hvac_system'),
    path('projects/fabricate-and-supply/', views.fabricate_and_supply, name='fabricate_and_supply'),
    path('projects/warehouses-project/', views.warehouses_project, name='warehouses_project'),
    path('projects/electrical-system-installation/', views.electrical_system_installation, name='electrical_system_installation'),

    # Services URLs
    path('services/', views.services, name='services'),
    path('services/building-services/', views.building_service, name='building-service'),
    path('services/mechanical-services/', views.mechanical_services, name='mechanical-services'),
    path('services/engineering-consultancy/', views.engineering_services, name='engineering-services'),
    path('services/agriculture-engineering/', views.agriculture_engineering_services, name='agriculture-engineering-services'),
]