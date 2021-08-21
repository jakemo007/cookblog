from django.urls import path
from .views import UserRegisteVieW

#Creating Urls
urlpatterns = [
    path("register",UserRegisteVieW.as_view(),name='register'),
]