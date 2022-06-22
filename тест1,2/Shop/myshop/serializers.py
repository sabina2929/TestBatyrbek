from rest_framework import serializers
from .models import Category,Product

class ProductSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    description=serializers.CharField()

