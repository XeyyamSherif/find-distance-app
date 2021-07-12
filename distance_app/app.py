from flask import Flask, abort, request
from geopy.geocoders import Nominatim
from geopy import distance
from flask import Blueprint
import logging
from flask import jsonify


logging.basicConfig(filename="distance.log", level=logging.DEBUG)

distance_app = Blueprint('distance_app', __name__)
geolocator = Nominatim(user_agent="distance_app")
geocoder = Nominatim(user_agent="Distance from MKAD")


'''This will give us Mkad coordinates'''
location = geolocator.geocode("Mkad")
coord_mkad = (location.latitude, location.longitude)


@distance_app.route('/')
def anan():
    return 'done'


@distance_app.route('/find_distance')
def index():
    '''you should send data as argument like key, value
    i suggest you use Postman
    '''
    if 'address' in request.args:
        try:
            location2 = geolocator.geocode(request.args.get('address'))
            specified_address = (location2.latitude, location2.longitude)
        except:
            return {
                'message': 'couldnt find adress, please enter address correctly'
            }
    else:
        try:
            latitude = float(request.args.get('latitude'))
            longitude = float(request.args.get('longitude'))
        except:
            return {
                'status': 'wrong input'
            }
        specified_address = (latitude, longitude)

    '''
    if you want to find distance with only longitude and latitude
    send data like this  example: 
    http://127.0.0.1:5000/find_distance?longitude=12&latitude=15
    but you can send exact address too 
    example:
    http://127.0.0.1:5000/find_distance?address=Istanbul
    '''

    distance_two_point = distance.distance(coord_mkad, specified_address)
    logging.debug(distance_two_point)

    return jsonify(
        distance=str(distance_two_point),
    )
