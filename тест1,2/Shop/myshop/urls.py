from django.urls import path
from .views import ProductView
from . import views

app_name="myshop"

urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('products/',ProductView.as_view()),
]