from django.db import models


class Category(models.Model):
    CategoryName=models.CharField(max_length=200)


    def __str__(self):
        return self.CategoryName


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description=models.TextField(blank=True)
    #available=models.BooleanField(default=True)
    #price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
