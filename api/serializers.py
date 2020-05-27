from farmers.models import FarmerDetails, Products
from rest_framework import serializers

class FamersInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = FarmerDetails
        fields = [
                'id', 'first_name', 'last_name', 'county', 'ward', 'village', 'phone_number', 'longitude', 'latitude',
                'nearest_town', 'national_id_no', 'passport_no', 'created_at', 'updated_at'
             ]

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'product_description', 'product_price', 'cover']