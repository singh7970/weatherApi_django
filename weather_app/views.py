from django.shortcuts import render
import requests
from .models import City

def index(request):
    api_key = '1d1f2219408b959f4d51fb52af919ddf'
    cities = City.objects.all()
    weather_data_list = []

    for city in cities:
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city.name, api_key)
        response = requests.get(url)

        # Check for errors in the API response
        response.raise_for_status()

        weather_data = response.json()

        city_name = weather_data['name']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        icon_code = weather_data['weather'][0]['icon']
        icon_url = 'https://openweathermap.org/img/wn/{}.png'.format(icon_code)

        context = {
            'city_name': city_name,
            'temperature': temperature,
            'description': description,
            'icon_url': icon_url,
        }
        weather_data_list.append(context)

    return render(request, 'weather.html', {'weather_data_list': weather_data_list})
