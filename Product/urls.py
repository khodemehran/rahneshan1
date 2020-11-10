from django.urls import path
from . import views



urlpatterns = [

    path('products/', views.product, name = "products"),
    path('products-detail/', views.product_detail, name = "product-detail"),

]

