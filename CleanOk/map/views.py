# # from django.shortcuts import render
# # import folium
# # from geopy import GoogleV3
# #
# # # Create your models here.
# # from geopy.geocoders import Nominatim
# # from IPython.display import display, HTML
# # from .models import MapsDjangoGeoMap
# #
# # # Create your views here.
# #
# #
# # def locations(request, place1 = "Красная площадь, Москва"):
# #     maps = MapsDjangoGeoMap.objects.all()
# #     place1 = "Красная площадь, Москва"
# #     geolocator = Nominatim(user_agent="cleanok")
# #     location = geolocator.geocode(place1)
# #     # location = GoogleV3(api_key="AIzaSyDUEQtZCw1FDYDFdXK6ZEEMEHQSa5KNZOE", domain="maps.google.ru").geocode(place1)
# #     latitude = location.latitude
# #     longitude = location.longitude
# #     loc = float(latitude), float(longitude)
# #     # print(location)
# #     m = folium.Map(location=loc, width=800, heigtht=400)
# #     # m._build_map()
# #     folium.Marker(loc, popup="Новосибирск").add_to(m)
# #     mapWidth, mapHeight = (400, 500)  # width and height of the displayed iFrame, in pixels
# #     # srcdoc = m.HTML.replace('"', '&quot;')
# #     embed = HTML('<iframe srcdoc="{}" '
# #                  'style="width: {}px; height: {}px; display:block; width: 50%; margin: 0 auto; '
# #                  'border: none"></iframe>'.format(m, mapWidth, mapHeight))
# #     # data = m.save('../CleanOk/templates/maps_django/map.html')
# #
# #     iframe = m._repr_html_()
# #     context = {
# #         'map': m,
# #     }
# #     return render(request, 'maps_django/map.html', context=context)
#
#
#
#
#
# # def index(request):
# #     posts = Women.objects.all()
# #     cats = Category.objects.all()
# #
# #     context = {
# #         'posts': posts,
# #         'cats': cats,
# #         'menu': menu,
# #         'title': 'Главная страница',
# #         'cat_selected': 0,
# #     }
# #
# #     return render(request, 'women/index.html', context=context)
#
# from django.shortcuts import render, get_object_or_404
# from .models import MapsDjangoGeoMap
# # from .forms import MeasurementModelForm
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
# # from .utils import get_geo, get_center_coordinates, get_zoom
# import folium
#
# from jinja2 import Environment, DictLoader
#
# # Create your views here.
#
# def calculate_distance_view(request):
#     # initial values
#     distance = None
#     destination = None
#
#     # obj = get_object_or_404(Measurement, id=1)
#     # form = MeasurementModelForm(request.POST or None)
#     # geolocator = Nominatim(user_agent='measurements')
#
#     ip = '72.14.207.99'
#     # country, city, lat, lon = get_geo(ip)
#     place1 = "Красная площадь, Москва"
#     geolocator = Nominatim(user_agent="cleanok")
#     location = geolocator.geocode(place1)
#     # location = geolocator.geocode(city)
#
#     # location coordinates
#     l_lat = location.latitude
#     l_lon = location.longitude
#     pointA = (l_lat, l_lon)
#     loc = float(l_lat), float(l_lon)
#
#     # initial folium map
#     m = folium.Map(width=800, height=500, location=loc, zoom_start=8)
#     # location marker
#     # folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
#     #               icon=folium.Icon(color='purple')).add_to(m)
#     #
#     # if form.is_valid():
#     #     instance = form.save(commit=False)
#     #     destination_ = form.cleaned_data.get('destination')
#     #     destination = geolocator.geocode(destination_)
#     #
#     #     # destination coordinates
#     #     d_lat = destination.latitude
#     #     d_lon = destination.longitude
#     #     pointB = (d_lat, d_lon)
#     #     # distance calculation
#     #     distance = round(geodesic(pointA, pointB).km, 2)
#     #
#     #     # folium map modification
#     #     m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon, d_lat, d_lon),
#     #                    zoom_start=get_zoom(distance))
#     #     # location marker
#     #     folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
#     #                   icon=folium.Icon(color='purple')).add_to(m)
#     #     # destination marker
#     #     folium.Marker([d_lat, d_lon], tooltip='click here for more', popup=destination,
#     #                   icon=folium.Icon(color='red', icon='cloud')).add_to(m)
#     #
#     #     # draw the line between location and destination
#     #     line = folium.PolyLine(locations=[pointA, pointB], weight=5, color='blue')
#     #     m.add_child(line)
#     #
#     #     instance.location = location
#     #     instance.distance = distance
#     #     instance.save()
#
#     m = m._repr_html_()
#     # with open('map.html', 'w') as writer:
#     #     writer.write(m)
#     data = MapsDjangoGeoMap.objects.get(pk=1)
#     data.choice_set.create(map=m)
#     context = {
#         'map': m,
#     }
#
#
#     return render(request, 'maps_django/map.html', context)
