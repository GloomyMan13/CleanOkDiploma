

from geopy.geocoders import Nominatim
import folium
from geopy import GoogleV3

# Create your models here.
from IPython.display import display, HTML
from ..models import HomePage

def write_code():
    """Функция для переписывания карты из медиа файла в другой темплэйт"""
    data = str()
    map_name_file = HomePage.objects.first().map_name_file

    with open(f'./media/map/{map_name_file}', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            data += line



    # map_file = open("./media/map/map.html", "r")
    #
    #
    #
    Html_file = open("./CleanOk/templates/map/map.html", "w")
    Html_file.write(data)
    Html_file.close()

    # m.save('mapss.html')



