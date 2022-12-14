"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, People, Planets, Favorites
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

"""
Get all users
"""

@api.route('/users', methods=['GET'])
def select_allUsers():
    users = User.query.all()
    allUsers = list(map(lambda user: user.serialize(), users))
    response_body = {
        "message": "This is your selected character"
    }

    return jsonify(allUsers), 200


"""
Get single user
"""

@api.route('/users/<int:id>', methods=['GET'])
def single_user(id):
    user = User.query.filter_by(id=id).first()
    response_body = {
        "message": "This is your selected character"
    }

    return jsonify(user.serialize()), 200


"""
Get all favorites
"""


@api.route('/favorites', methods=['GET'])
def get_favorites():
    favorite_query=Favorites.query.all()
    all_favorites=list(map(lambda x:x.serialize(), favorite_query))

    return jsonify(all_favorites), 200


"""
Get favorites of a user
"""

@api.route('/users/favorites/<int:id>', methods=['GET'])
def user_favorites(id):
    user_fav = User.query.filter_by(id=id).first()
    response_body = {
        "message": "This is your selected character"
    }

    return jsonify(user_fav.favorites.serialize()), 200


"""
Get all characters
"""

@api.route('/people', methods=['GET'])
def select_allCharacters():
    people = People.query.all()
    allPeople = list(map(lambda character: character.serialize(), people))
    response_body = {
        "message": "This is your selected character"
    }

    return jsonify(allPeople), 200


"""
Get single character
"""

@api.route('/people/<int:id>', methods=['GET'])
def selected_character(id):
    person = People.query.filter_by(id=id).first()
    response_body = {
        "message": "This is your selected character"
    }

    return jsonify(person.serialize()), 200


"""
Get all planets
"""

@api.route('/planets', methods=['GET'])
def select_allPlanets():
    planets = Planets.query.all()
    allPlanets = list(map(lambda planet: planet.serialize(), planets))
    response_body = {
        "message": "This is your selected planet"
    }

    return jsonify(allPlanets), 200

"""
Get single planet
"""

@api.route('/planets/<int:id>', methods=['GET'])
def selected_planet(id):
    planet = Planets.query.filter_by(id=id).first()
    response_body = {
        "message": "This is your selected character"
    }

    return jsonify(planet.serialize()), 200

"""
Add new character
"""

@api.route('/people/<int:id>', methods=['POST'])
def add_people(id):    
    new = request.get_json()
    new_person = People(id=id, name=new["name"])
    db.session.add(new_person)
    db.session.commit()

    return jsonify("A new person was added."), 200

"""
Add new planet
"""

@api.route('/planets/<int:id>', methods=['POST'])
def add_planet(id):    
    new = request.get_json()
    new_planet = Planets(id=id, name=new["name"])
    db.session.add(new_planet)
    db.session.commit()

    return jsonify("A new planet was added."), 200


"""
Add new character to favorites list
"""

@api.route('/favorites/people/<int:id>', methods=['POST'])
def add_favorite_people(id):    
    new = request.get_json()
    new_favorite_person = Favorites(user_id=id, character_name=new["character_name"],  planet_name=None)
    db.session.add(new_favorite_person)
    db.session.commit()

    return jsonify("A new person was added to favorites."), 200

"""
Add new planet to favorites list
"""

@api.route('/favorites/planets/<int:id>', methods=['POST'])
def add_favorite_planet(id):    
    new = request.get_json()
    new_favorite_planet = Favorites(user_id=id, planet_name=new["planet_name"], character_name=None)
    db.session.add(new_favorite_planet)
    db.session.commit()

    return jsonify("A new planet was added to favorites."), 200


"""
Delete character directly from characters
"""    

@api.route('/people/<int:id>', methods=['DELETE'])
def delete_people(id):
    deleted_person = People.query.get(id)
    if deleted_person == None:
        return("This person does not exist."), 200
    elif deleted_person.name is None:
        return("This is not a character."), 200
    else:
        db.session.delete(deleted_person)
        db.session.commit()
        return jsonify("Person was deleted."), 200 

"""
Delete planet directly from planets
"""    

@api.route('planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
    deleted_planet = Planets.query.get(id)
    if deleted_planet == None:
        return("This planet does not exist."), 200
    elif deleted_planet.name is None:
        return("This is not a planet."), 200
    else:
        db.session.delete(deleted_planet)
        db.session.commit()
        return jsonify("Planet was deleted."), 200 

"""
Delete character from favorites list
"""    

@api.route('/favorites/people/<int:id>', methods=['DELETE'])
def delete_favorite_people(id):
    deleted_person = Favorites.query.get(id)
    if deleted_person == None:
        return("This person does not exist."), 200
    elif deleted_person.character_name is None:
        return("This is not a character."), 200
    else:
        db.session.delete(deleted_person)
        db.session.commit()
        return jsonify("Person was deleted from favorites."), 200    

"""
Delete planet from favorites list
"""    

@api.route('/favorites/planets/<int:id>', methods=['DELETE'])
def delete_favorite_planet(id):
    deleted_planet = Favorites.query.get(id)
    if deleted_planet == None:
        return("This planet does not exist."), 200
    elif deleted_planet.planet_name is None:
        return("This is not a planet."), 200
    else:
        db.session.delete(deleted_planet)
        db.session.commit()
        return jsonify("Planet was deleted from favorites."), 200 
