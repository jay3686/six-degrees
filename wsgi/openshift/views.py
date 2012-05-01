import os
import pymongo
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse


connection = pymongo.Connection('localhost', 27017)
db = connection.six


""" Takes in a MongoDB collection and returns JSON. """
def mongo_to_json(collection):
    doc_list = list(collection)
    # Removing MongoDB document ID's as they don't convert well to JSON.
    for doc in doc_list:
        if doc.has_key('_id'):
            del doc['_id']
    
    # dumps converts a python dict to JSON
    return simplejson.dumps(output)


def home(request):
    return render_to_response('home/home.html')


""" Takes in movie title and year and returns a JSON list of actors in movie. """
def get_actors(request):
    title = request.GET['title']
    year = request.GET['year']

    adb = db.actors.find({"mkey": title + year },{ 'name' : 1})
    return HttpResponse(mongo_to_json(adb), mimetype='application/javascript')


""" Takes in an actor name and returns a JSON list of moviie titles / release years. """
def get_movies(request):
    name = request.GET['name']

    adb = db.actors.find({"name": name },{ 'movies' : 1})
    return HttpResponse(mongo_to_json(adb), mimetype='application/javascript')


""" Takes in an partial string and returns a JSON list of matching actor names. """
def get_actor_list(request):
    name = request.GET['name']


    adb = db.actors.find({"name": { '$regex' : name }},{ 'name' : 1})

    return HttpResponse(mongo_to_json(adb), mimetype='application/javascript')
