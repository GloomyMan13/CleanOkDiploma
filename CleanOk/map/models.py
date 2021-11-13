# myapp/models.py
from wagtail.core.models import Page
from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField


from wagtail.admin.edit_handlers import FieldPanel
import folium
from geopy import GoogleV3
from .locations.locations import locations
# Create your models here.
from geopy.geocoders import Nominatim
from IPython.display import display, HTML


class MapsDjangoGeoMap(Page, models.Model):
    template = "maps_django/map_page.html"
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    loc = display(locations(location))
    map =  str(locations(location))


    content_panels = Page.content_panels + [
        FieldPanel("location"),
        FieldPanel("destination"),
        FieldPanel("distance"),
    ]

    def __str__(self):
        return f"Distance from {self.location} to {self.destination} is {self.distance} km"