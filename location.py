import webbrowser, requests
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder

def loc(place):
    webbrowser.open("http://www.google.com/maps/place/" + place + "")
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(place, addressdetails=True)
    target_latlng = location.latitude, location.longitude
    location = location.raw['address']
    target_loc = {'city': location.get('city', ''),
                   'state': location.get('state', ''),
                   'country': location.get('country', '')}
    current_loc = geocoder.ip('me')
    current_latlng = current_loc.latlng

    distance = str(great_circle(current_latlng, target_latlng))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance), 2)

    return current_loc, target_loc, distance

def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']
    #print(city,state,country)
    return city, state,country


# import time
# #loc('Accra')
# #my_location()
# command=input('>>')
# if "where is" in command:
#         place = command.split('where is ', 1)[1]
#         current_loc, target_loc, distance =loc(place)
#         city = target_loc.get('city', '')
#         state = target_loc.get('state', '')
#         country = target_loc.get('country', '')
#         time.sleep(1)
#         try:

#             if city:
#                 res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
#                 print(res)
#                 #speak(res)

#             else:
#                 res = f"{state} is a state in {country}. It is {distance} km away from your current location"
#                 print(res)
#                 #speak(res)

#         except:
#             res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
#             print(res)
#             #speak(res)


# elif "current location" in command or "where am i" in command:
#     try:
#         city, state, country = my_location()
#         print(city, state, country)
#         #speak(f"You are currently in {city} city which is in {state} state and country {country}")
#     except Exception as e:
#         print(e)
#         #speak("Sorry sir, I coundn't fetch your current location. Please try again")