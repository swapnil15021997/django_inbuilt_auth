from rest_framework import serializers
from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



    def validate_name(self,value):
        if not value:
            raise serializers.ValidationError("Please provide product name")
        
        return value

    def validate_price(self,value):
        if not value:
            raise serializers.ValidationError("Please provide price of product")

        if value < 0:
            raise serializers.ValidationError("Product price not less than 0")  
        
        if value > 100:
            raise serializers.ValidationError("Price is greater than 100")

        return value