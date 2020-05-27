from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class FarmerDetails(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    county = models.CharField(max_length=120)
    ward  = models.CharField(max_length=120)
    village = models.CharField(max_length=120)
    longitude = models.CharField(max_length=250)
    latitude = models.CharField(max_length=250)
    nearest_town = models.CharField(max_length=200)
    national_id_no = models.IntegerField(blank=True)
    passport_no  = models.IntegerField(blank=True)
    phone_number = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=False, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True)
    
    class Meta:
        verbose_name_plural = 'FarmersInfo' 

    def __str__(self):
        return self.first_name

def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.name), filename])

class Products(models.Model):
    name = models.CharField(max_length=200)
    product_description = models.TextField(blank=True, default="A sample product text")
    product_price = models.IntegerField()
    cover = models.ImageField(blank=True, upload_to=upload_path)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Products'

    def __str__(self):
        return '%s' % (self.name)
