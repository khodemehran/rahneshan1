from django.urls import path
from .views import signup,loginview,logout_view

urlpatterns = [
    path('signup/', signup, name = "signup"),
    path('login/', loginview, name = "login"),
    path('logout_view/', logout_view, name = "logout"),
]
