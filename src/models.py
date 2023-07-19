import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
  
class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(Integer)
    gender = Column(String(250))
    height = Column(Integer)
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    favorites = relationship('Favorites', backref='characters', lazy=True)
    

    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(20))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    favorites = relationship('Favorites', backref='planets', lazy=True)

    def to_dict(self):
        return {}
    
class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(20))
    cargo_capacity = Column(Integer)
    consumables = Column(String(10))
    passengers = Column(Integer)
    crew = Column(String(250))
    favorites = relationship('Favorites', backref='vehicles', lazy=True)

    def to_dict(self):
        return {}
    
class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    def to_dict(self):
        return {}
    
class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    favorites = relationship('Favorites', backref='users', lazy=True)
    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
