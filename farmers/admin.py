from django.contrib import admin
from farmers.models import FarmerDetails, Products

class FarmersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'village', 'ward']

admin.site.register(FarmerDetails, FarmersAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_price']
    
admin.site.register(Products, ProductsAdmin)
