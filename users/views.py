from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.http import HttpResponse
from .models import Search,coordinate
from .forms import SearchForm
import folium
import geocoder
from .models import coordinate
import requests
import json

# def coordinate_list(request):
#      l=coordinate.objects.all()
#      #print(l.name)
#      print(l.latitude)
#      print(l.longtitue)
#      return(l)

def home(request):
    return render(request,'users/home.html')

def about(request):
    return render(request,'users/about.html')


@login_required
def profile(request):
    return render(request,'users/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')

    # Create Map Object
    # d=coordinate_list(request)
    # latit=d.latitude
    # longit=d.longitude
    # #print(latit)
    # # print(longit)
   

    m = folium.Map(location=[52, 60], zoom_start=3)

    folium.Marker([lat, lng], tooltip='Click for more',
                  popup=country).add_to(m)
    folium.Marker([26.7671509,75.851424],tooltip='Available',popup='India').add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
         'form': form,
    }
    return render(request, 'users/index.html', context)

# def i(request):
#      ip = requests.get('https://api64.ipify.org?format=json')
#      ip_data = json.loads(ip.text)
#       #print(ip_data)
#      res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
#      location_data_one = res.text
#      location_data = json.loads(location_data_one)
#      print("location_data")

     #return render(request, 'index.html', {'data': location_data})



# def get_ip():
#      response = requests.get('https://api64.ipify.org?format=json').json()
#      return response["ip"]


# def get_location():
#      ip_address = get_ip()
#      response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
#      location_data = {
#         "ip": ip_address,
#         "city": response.get("city"),
#         "region": response.get("region"),
#         "country": response.get("country_name"),
#         "latitude":response.get("latitude"),
#         "longitude":response.get("longitude"),
#      }
#     print("hi there")
#     print(location_data['ip'])
#     location_instance = coordinate (
#     name=location_data['city'],
#     latitude=location_data['latitude'],
#     longitude=location_data['longitude']

#     )
#     location_instance.save()
#     #location.save()
    
#     return location_data


# print(get_location())
# #print(get_location['city'])