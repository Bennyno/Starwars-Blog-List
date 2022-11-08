"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/character')
def selected_character():

    response_body = {
        "message": "This is your selected character"
    }

    return jsonify(response_body), 200

@api.route('/planet')
def selected_planet():

    response_body = {
        "message": "This is your selected planet"
    }

    return jsonify(response_body), 200

@api.route('/favorites', methods=['GET'])
def get_favorites():
    favorite_query=Favorites.query.all()
    all_favorites=list(map(lambda x:x.serialize(), favorite_query))

    return jsonify(all_favorites), 200

@api.route('/favorites/<int:id>', methods=['POST'])
def create_favorite():
    body=request.json
    # favorite=