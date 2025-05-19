from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def about2(request):
    return render(request, 'about2.html')  # Render the about2.html template

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')

def clients(request):
    return render(request, 'clients.html')

def values(request):
    return render(request, 'values.html')  # Render the values.html template

def licenses(request):
    return render(request, 'licenses.html')  # Render the licenses.html template

# Projects Views
def projects(request):
    return render(request, 'projects/projects.html')

def water_supply_system(request):
    return render(request, 'projects/water_supply_system.html')

def air_conditioner_installation(request):
    return render(request, 'projects/air_conditioner_installation.html')

def rehabilitation_project(request):
    return render(request, 'projects/rehabilitation_project.html')

def installation_of_hvac_system(request):
    return render(request, 'projects/installation_of_hvac_system.html')

def fabricate_and_supply(request):
    return render(request, 'projects/fabricate_and_supply.html')

def warehouses_project(request):
    return render(request, 'projects/warehouses_project.html')

def electrical_system_installation(request):
    return render(request, 'projects/electrical_system_installation.html')

# Services Views
def services(request):
    return render(request, 'services/services.html')

def building_service(request):
    return render(request, 'services/building_services.html')

def mechanical_services(request):
    return render(request, 'services/mechanical_services.html')

def engineering_services(request):
    return render(request, 'services/engineering_services.html')

def agriculture_engineering_services(request):
    return render(request, 'services/agriculture_engineering_services.html')

