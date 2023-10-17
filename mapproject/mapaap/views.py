from django.shortcuts import render
from .models import Restaurant, Rentalcars

def home_view(request):
    restaurants = Restaurant.objects.all()
    rental_cars = Rentalcars.objects.all()
    return render(request, 'mapaap/home.html', {'restaurants': restaurants, 'rental_cars': rental_cars})


def contact_us(request):
    if request.method == 'POST':
        # Handle form submission here (e.g., send emails, save data)
        # You can use Django forms to handle form validation and processing
        return render(request, 'mapaap/contact_us.html')
    
    # For GET requests, render the "contact_us.html" template
    return render(request, 'mapaap/contact_us.html')


def map_view(request):
    # Implement your map_view logic here
    # For example, fetch map data and render a template
    return render(request, 'mapaap/map.html')

def search_view(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        
        # Implement search logic here, for example, searching in restaurant names
        results = Restaurant.objects.filter(name__icontains=query)
        
        return render(request, 'mapaap/search_results.html', {'results': results})

def real_estate_view(request):
    # Fetch real estate data here if applicable
    # properties = RealEstate.objects.all()
    
    return render(request, 'mapaap/real_estate.html', {})

def currency_exchange_view(request):
    # Fetch currency exchange rates here if applicable
    # rates = CurrencyExchangeRate.objects.all()
    
    return render(request, 'mapaap/currency.html', {})


def contact_us(request):
    if request.method == 'POST':
           form_submitted = True
    return render(request, 'mapaap/contact_us.html', {'form_submitted': form_submitted})
    

from django.shortcuts import render, redirect
from .models import ContactMessage

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the message to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Redirect to the thank you page after form submission
        return redirect('thank_you')

    return render(request, 'mapaap/contact_us.html')




def thank_you(request):
    return render(request, 'mapaap/thank_you.html')


# views.py
import requests
from django.http import JsonResponse

def get_weather(request, city):
    api_key = 'e8c31967e15c6121f9b2be5656b633f3'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Get temperature in Celsius
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        city_name = data['name']
        return JsonResponse({'temperature': temperature, 'cityName': city_name})
    else:
        return JsonResponse({'error': 'City not found'}, status=404)




