from .models import Product, ProductStatus
from rest_framework import serializers



class ProductStatusSerilizer(serializers.ModelSerializer):    
    class Meta:
        model = ProductStatus
        fields = ('__all__')   

class ProductSerializer(serializers.ModelSerializer):
    status = ProductStatusSerilizer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('name', 'brand', 'status')