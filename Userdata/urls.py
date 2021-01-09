from django.urls import path
from .views import user_data, about, contact, home

urlpatterns = [

    path('user_data/', user_data, name = "user_data"),
    path('home/', home, name = "home"),
    path('contact/', contact, name = "contact"),
    path('about/', about, name = "about"),

]