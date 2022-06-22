from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView,View
from .serializers import ProductSerializer




def post_list(request):
    products=Product.objects.all()
    return render(request,'myshop/index.html',{'products':products})

class ProductView(View):
    def get(self,request):
        products=Product.objects.all()
        product_serialized_data=[]
        for product in products:
            product_serialized_data.append({
                'product_name':product.name,
                'description_name':product.description
            })
        data={
            'products':product_serialized_data
        }
        return  JsonResponse(data)

