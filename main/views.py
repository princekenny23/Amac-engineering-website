from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.shortcuts import render, redirect



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



def team(request):
    return render(request, 'team.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Format WhatsApp message
            full_message = f"New Contact Request from AMAC Website:\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
            phone_number = '265997575865'  # Replace with your WhatsApp number
            encoded_message = full_message.replace(' ', '%20').replace('\n', '%0A')
            whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"
            
            return redirect(whatsapp_url)
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
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

def message(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # You can process the form here (send email, save, etc.)
            success = True
            form = ContactForm()  # Reset form after success
    else:
        form = ContactForm()
    return render(request, 'message.html', {'form': form, 'success': success})

