from rest_framework import serializers
from api.models import ProductTable


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTable
        fields = ('sku','name','price','description','category','created_at')
        
    