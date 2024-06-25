from django.shortcuts import render, HttpResponse
import requests

def index(request):
    city = request.GET.get('city', 'Kathmandu')  # Set default city to Kathmandu
    api_key = 'Your weather API'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
    # Check if the city was found in the API response
    if response.status_code == 200:
        city = data['name']
        humidity = data['main']['humidity']
        windspeed = data['wind']['speed']
        tempr = data['main']['temp']
        tempr = tempr - 273.15  # Convert temperature from Kelvin to Celsius
        tempr = round(tempr, 2)
        image = data['weather'][0]['icon']
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        return render(request, 'index.html', {
            'city': city,
            'humidity': humidity,
            'windspeed': windspeed,
            'tempr': tempr,
            'image': image,
            'latitude': latitude,
            'longitude': longitude
        })
    else:
        return HttpResponse(f"City {city} not found.", status=404)






                                  
                                    