import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False, unique=True)

class Planet_Properties(Base):
    __tablename__ = "planet_properties"
    id = Column(Integer, primary_key=True)
    planet_id = Column(ForeignKey('planet.id'))
    name = Column(ForeignKey('planet.name'))
    climate = Column(String, nullable=False)
    created = Column(String, nullable=False)
    diameter = Column(String, nullable=False)
    films = Column(String, nullable=False)
    gravity = Column(String, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    residents = Column(String, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    surface_water = Column(Integer, nullable=False)
    terrain = Column(String, nullable=False)
    url = Column(String, nullable=False, unique=True)


class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False, unique=True)  

class Vehicle_Properties(Base):
    __tablename__ = "vehicle_properties"
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(ForeignKey('vehicle.id'))
    name = Column(ForeignKey('vehicle.name'))
    cargo_capacity = Column(Integer, nullable=False)
    created = Column(String, nullable=False)
    crew = Column(Integer, nullable=False)
    length = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    model = Column(String, nullable=False)
    vehicle_class = Column(String, nullable=False)
    passengers = Column(Integer, nullable=False)
    pilots = Column(String, nullable=False)
    films = Column(String, nullable=False)
    url = Column(String, nullable=False)    



## Draw from SQLAlchemy base
render_er(Base, "diagram.png")
