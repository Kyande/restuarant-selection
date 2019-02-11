# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
import os
import clips

from .models import Restaurant, Review


# Create your views here.
<<<<<<< HEAD
def index(request):
    return render(request, 'restuarant_app/index.html', {'text': "hello world"})


def suggestions(request):
    return render(request, 'restuarant_app/suggestions.html', {})


def about_us(request):
    return render(request, 'restuarant_app/about.html', {})
=======
def home(request):
    return render(request, 'restuarant_app/home.html', {})


def details(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    reviews = Review.objects.filter(restaurant=restaurant)
    return render(request, 'restuarant_app/details.html', {
        'restaurant': restaurant,
        'reviews': reviews
    })


def suggestions(request):
    results = query_clips(request.POST)
    print(results)
    ids = []
    #prepare response.
    if results is not None:
        results = results.split("---")
        for result in results:
            if len(result) > 0:
                ids.append(int(result.split(",")[0].encode('utf-8')))
    # get restaurants from DB.
    restaurants = Restaurant.objects.filter(restaurant_id__in=ids).order_by('restaurant_id')
    # import pdb; pdb.set_trace()
    return render(request, 'restuarant_app/suggestions.html', {
        'restaurants': restaurants,
    })


def query_clips(data):
    if data['place'] == 'cbd':
        place = data['place'].upper()
    else:
        place = data['place'].capitalize()

    preference =\
        """
        (preferences (budget "{0}") 
                     (location "{1}") 
                     (cuisine "{2}") 
                     (experience "{3}") 
                     (has-delivery "{4}") 
                     (rating "?") 
                     (has-alcohol "{5}") 
                     (has-vegetarian "{6}"))
        """.format(
            data['price'].capitalize(),
            place,
            data['cuisine'].capitalize(),
            data['ambiance'].capitalize(),
            data['delivery'].upper(),
            data['alcohol'].upper(),
            data['vegetarian'].upper()
        ).encode('utf-8').lstrip().rstrip()
    # run clips
    clips.Clear()
    clips.BatchStar(settings.CLIPS_DIR + "templates.clp")
    clips.BatchStar(settings.CLIPS_DIR + "rules.clp")
    if os.path.isfile(settings.CLIPS_DIR + "restaurants.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "restaurants.clp")
    clips.Reset()
    clips.Assert(preference)
    clips.Run()
    return clips.StdoutStream.Read()
>>>>>>> ui-for-clips
