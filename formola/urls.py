from django.urls import path
from .views import index, userinput


urlpatterns = [
    path('planet/', index, name = "planetlist"),
    path('userinput/', userinput, name = "userinput"),
    
]
