from django.contrib import admin

# Register your models here.

from . models import Category,Product
admin.site.register(Category)
admin.site.register(Product)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','available','price']
    list_filter = ['available']
