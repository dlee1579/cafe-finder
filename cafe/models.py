from django.db import models
from address.models import AddressField

# Create your models here.
class Cafe(models.Model):
    name = models.CharField(max_length=50)
    address1 = AddressField(blank=True, null=True)
    address2 = AddressField(related_name='+', blank=True, null=True)
    number_seats = models.IntegerField(blank=True, null=True)
    type_seats = models.CharField(max_length=25, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    neighborhood = models.CharField(max_length=25, blank=True, null=True)
    has_wall_outlets = models.BooleanField(blank=True, null=True)
    is_pet_friendly = models.BooleanField(blank=True, null=True)
    # thumbnail_url = models.URLField(max_length=200, blank=True, null=True)
    thumbnail_image_location = models.TextField(max_length=200, blank=True, null=True)
    google_maps_url = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name