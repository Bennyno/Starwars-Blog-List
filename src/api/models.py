from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # username = db.Column(db.String(250), unique= True, nullable = False)
    # user_password = db.Column(db.String, nullable=False)
    favorites = db.relationship("Favorites", back_populates="user")

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=False, nullable=False)
    user = db.relationship("User", back_populates="favorites")
    # favorite_planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"))
    # favorite_planet = db.relationship("Planets")
    # favorite_character_id = db.Column(db.Integer, db.ForeignKey("people.id"))
    # favorite_character = db.relationship("People")
    planet_name = db.Column(db.String, nullable=False)
    character_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Favorites {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "character_name": self.character_name,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    height = db.Column(db.String(250))
    mass = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250), nullable=True)
    eye_color = db.Column(db.String(250), nullable=True)
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250), nullable=True)
    homeworld_id = db.Column(db.Integer, db.ForeignKey("planets.id"))
    homeworld = db.relationship("Planets")
    
    def to_dict(self):
        return {}

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    rotation_period = db.Column(db.String(250))
    orbital_period = db.Column(db.String(250))
    diameter = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    gravity = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.String(250))
    population = db.Column(db.String(250))
    people= db.relationship("People")

    def to_dict(self):
        return {}

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

# class Vehicles(db.Model):
#     __tablename__ = "vehichles"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250))
#     model = db.Column(db.String(250))
#     manugacturer = db.Column(db.String(250))
#     cost_in_credits = db.Column(db.Integer)
#     length = db.Column(db.Integer)
#     cargo_capacity = db.Column(db.Integer)
#     vehicle_class = db.Column(db.String(250))