from django.shortcuts import render
from .models import location
import requests
#import geocoder
#import folium
import json
#g=geocoder.ip("me")
#myAddress=g.latlng 
#my_map1=folium.map(location=myAddress,zoom_start=12)
#my_map1.save("my_map.html")

# # Create your views here.
def index(request):
    ip = requests.get('https://api64.ipify.org?format=json')
    ip_data = json.loads(ip.text)
     #print(ip_data)
    res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    print("location_data")

    #return render(request, 'index.html', {'data': location_data})



#def index(request):
#    print("1. Starting index function")
#   ip = requests.get('https://api64.ipify.org?format=json')
#
#   print(f"2. Got IP: {ip.text}")
#   ip_data = json.loads(ip.text)
#    res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
#    print(f"3. Got location data: {res.text}")
#    location_data_one = res.text
#    location_data = json.loads(location_data_one)
#    print(f"4. Parsed location data: {location_data}")
#
#    return render(request, 'index.html', {'data': location_data})

#
# import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "latitude":response.get("latitude"),
         "longitude":response.get("longitude"),
    }
    print("hi there")
    print(location_data['ip'])
    location_instance = location (
        name=location_data['city'],
        latitude=location_data['latitude'],
        longitude=location_data['longitude']

    )
    location_instance.save()
    #location.save()
    
    return location_data


print(get_location())
#print(get_location['city'])





    
