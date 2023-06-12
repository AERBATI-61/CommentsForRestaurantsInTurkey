from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('retaurantDetail/<str:id>', retaurantDetail, name='restaurantDetail'),
    path('aboutme', AboutMe.as_view(), name='aboutMe'),
    path('foods', food, name='food'),
    path('commetns', comment, name='comment'),
    path('cities', city, name='city'),
]