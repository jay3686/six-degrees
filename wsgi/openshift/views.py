import os
import pymongo
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse


connection = pymongo.Connection('mongodb://admin:4A5buhckPFSw@127.6.89.1:27017/')
#connection = pymongo.Connection('localhost', 27017)
db = connection.six

def home(request):
    return render_to_response('home/home.html')


#input:  movie title and year
#output:    json list of actors in movie
def getActors(request):
    title = request.GET['title']
    year = request.GET['year']

    adb = db.actors.find({"mkey": title + year },{ 'name' : 1})

    return HttpResponse(adb, mimetype='application/javascript')


#input:  actor name
#output:    json list of movie title and year
def getMovies(request):
    name = request.GET['name']

    adb = db.actors.find({"name": { '$regex' : name }},{ 'movies' : 1})

    return HttpResponse(adb, mimetype='application/javascript')


def getActorList(request):
    name = request.GET['name']


    adb = db.actors.find({"name": { '$regex' : name }},{ 'name' : 1})
    return HttpResponse(json.dumps(adb), mimetype='application/javascript')
