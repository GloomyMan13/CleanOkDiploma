# from geopy import GoogleV3
#
# place = "Красная площадь, Москва"
# location = GoogleV3(api_key="AIzaSyA9-lxOdXf2DrCjZUxSpEUXaWhllxOacF0").geocode(place)
#
# print(location.address)
# print(location.latitude, location.longitude)

from geopy.geocoders import Nominatim
import folium
from geopy import GoogleV3

# Create your models here.
from IPython.display import display, HTML
# geolocator = Nominatim(user_agent="cleanok")
# location = geolocator.geocode("Красная площадь, Москва")
# print(location.latitude)

def locations(place1 = "Красная площадь, Москва"):
    place1 = "Улица ленина, Хабаровск"
    geolocator = Nominatim(user_agent="cleanok")
    location = geolocator.geocode(place1)
    latitude1 = location.latitude
    longitude1 = location.longitude
    loc1 = float(latitude1), float(longitude1)
    # print(location)
    m = folium.Map(location=loc1, zoom_start=4, width=1500, heigtht=100)
    # m._build_map()
    place2 = "Красная площадь, Москва"
    location = geolocator.geocode(place2)
    latitude = location.latitude
    longitude = location.longitude
    loc = float(latitude), float(longitude)
    folium.Marker(location=loc, popup="Красная площадь, Москва").add_to(m)
    folium.Marker(location=loc1, popup="Улица Ленина, Хабаровск").add_to(m)

    iframe = m._repr_html_()

    Html_file = open("./CleanOk/templates/maps_django/map.html", "w")
    Html_file.write(iframe)
    Html_file.close()

    return iframe

