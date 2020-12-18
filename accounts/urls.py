from django.urls import path
from .views import signup,loginview

urlpatterns = [
    path('signup/', signup, name = "signup"),
    path('login/', loginview, name = "login"),
]
