from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView

from .models import *


def index(request):
    destination = request.GET.get('destination')
    if destination == None:
        restaurants = Restaurants.objects.all()
    else:
        restaurants = Restaurants.objects.filter(destination__destination=destination)
    context = {
        'destinations': Destination.objects.all(),
        'cities': City.objects.filter(destination__destination=destination),
        'restaurant_destinations': restaurants,
        'restaurant_cities': Restaurants.objects.filter(city__sehir_name=destination),
        'food_count': Food.objects.all(),
        'comment_count': Comment.objects.all(),
        'user_count': User.objects.all(),
    }
    return render(request, 'comments/index.html', context)




def city(request):

    context = {
    'restaurant_destinations': Restaurants.objects.all(),

    }
    return render(request, 'comments/city.html', context)







def retaurantDetail(request, id):
    restaurantDetails = Restaurants.objects.get(id=id)
    total = []
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        waiter = request.POST.get("waiter")
        park = request.POST.get("park")
        comfortable = request.POST.get("comfortable")
        air_condition = request.POST.get("air_condition")
        cleaning = request.POST.get("cleaning")
        flavor = request.POST.get("flavor")
        price = request.POST.get("price")
        menu_variety = request.POST.get("menu_variety")
        description = request.POST.get("description")
        newComment = Comment(
            name=name, email=email, waiter=waiter, park=park, comfortable=comfortable, air_condition=air_condition,
            cleaning=cleaning, flavor=flavor, price=price, menu_variety=menu_variety, description=description, )
        newComment.restaurant = restaurantDetails
        newComment.save()
        return redirect(reverse("restaurantDetail", kwargs={"id": id}))
    for i in Comment.objects.filter(restaurant=id):
        orts = (int(i.waiter) + int(i.park) + int(i.comfortable) + int(i.air_condition) + int(i.cleaning) + int(
            i.flavor) + int(i.price) + int(i.menu_variety)) // 8
        total.append(orts)
    total = sum(total)
    total_ort = 0
    if (Comment.objects.filter(restaurant=id)):
        total_ort = float(total) / float(Comment.objects.filter(restaurant_id=id).count())
    context = {
        'restaurantDetails': restaurantDetails,
        'comments': Comment.objects.order_by("-date").filter(restaurant_id=id),
        'total_ort': total_ort,
        'foods': Food.objects.filter(restaurant_id=id)[:3]
    }
    return render(request, 'comments/restaurantDetail.html', context)


def food(request):
    context = {
        'foods': Food.objects.all()
    }
    return render(request, 'comments/foods.html', context)


def comment(request):
    context = {
        'comments': Comment.objects.order_by("-date").all()
    }
    return render(request, 'comments/all_comments.html', context)


class AboutMe(ListView):
    model = AboutMe
    context_object_name = 'managers'
    template_name = 'comments/about_Me.html'
