import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    password = Column(String)
    email = Column(String)
    preference_id = Column(Integer, ForeignKey('preference.id'))
    preference = relationship("Preference")

class Preference(Base):
    __tablename__ = 'preference'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    films_id = Column(Integer, ForeignKey('film.id'))
    film = relationship("Film")
    users = relationship("User", back_populates="preference")

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_year = Column(String)
    films_id = Column(Integer, ForeignKey('film.id'))
    gender = Column(String)
    hair_color = Column(String)
    height = Column(Integer)
    homeworld_id = Column(Integer, ForeignKey('planet.id'))
    mass = Column(Integer)
    skin_color = Column(String)
    edited = Column(Integer)
    starships_id = Column(Integer, ForeignKey('starship_vehicles.id'))
    vehicles_id = Column(Integer, ForeignKey('starship_vehicles.id'))
    species_name = Column(String)
    classification = Column(String)
    designation = Column(String)
    average_height = Column(String)
    average_lifespan = Column(String)
    eye_colors = Column(String)
    hair_colors = Column(String)
    language = Column(String)
    homeworld = relationship("Planet")
    films = relationship("Film", back_populates="characters")
    starships = relationship("StarshipVehicle", foreign_keys=[starships_id])
    vehicles = relationship("StarshipVehicle", foreign_keys=[vehicles_id])

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    climate = Column(String)
    created = Column(Integer)
    diameter = Column(Integer)
    edited = Column(Integer)
    films_id = Column(Integer, ForeignKey('film.id'))
    gravity = Column(String)
    orbital_period = Column(Integer)
    population = Column(Integer)
    residents = Column(String)
    rotation_period = Column(Integer)
    surface_water = Column(Integer)
    terrain = Column(String)
    url = Column(String)
    films = relationship("Film", back_populates="planets")

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('people.id'))
    created = Column(Integer)
    director = Column(String)
    episode_id = Column(Integer)
    opening_crawl = Column(String)
    planets_id = Column(Integer, ForeignKey('planet.id'))
    producer = Column(String)
    release_date = Column(Integer)
    starships_id = Column(Integer, ForeignKey('starship_vehicles.id'))
    title = Column(String)
    url = Column(String)
    vehicles_id = Column(Integer, ForeignKey('starship_vehicles.id'))
    characters = relationship("People", back_populates="films")
    planets = relationship("Planet", back_populates="films")
    starships = relationship("StarshipVehicle", back_populates="films")
    vehicles = relationship("StarshipVehicle", back_populates="films")

class StarshipVehicle(Base):
    __tablename__ = 'starship_vehicles'
    id = Column(Integer, primary_key=True)
    type_of_vehicle = Column(String)
    name = Column(String)
    model = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    length = Column(String)
    passengers = Column(String)
    max_atmosphering_speed = Column(String)
    hyperdrive_rating = Column(String)
    MGLT = Column(String)
    cargo_capacity = Column(String)
    consumables = Column(String)
    films_id = Column(Integer, ForeignKey('film.id'))
    pilot_id = Column(Integer, ForeignKey('people.id'))
    crew = Column(String)
    url = Column(String)
    created = Column(String)
    edited = Column(String)
    films = relationship("Film", back_populates="starships")
    pilot = relationship("People", back_populates="starships")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
