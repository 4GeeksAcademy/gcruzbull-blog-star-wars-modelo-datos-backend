from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
import enum

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(20), nullable = False)
    last_name: Mapped[str] = mapped_column(String(20), nullable = False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="user_table")

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Favorite(db.Model):
    __tablename__ = "favorite"

    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=False)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    user_table: Mapped["User"] = relationship("User", back_populates="favorites")
    character_table: Mapped["Character"] = relationship("Character", back_populates="favorites")
    planet_table: Mapped["Planet"] = relationship("Planet", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        }

    
class Character(db.Model):
    __tablename__ = "character"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable = False)
    height: Mapped[int] = mapped_column(Integer)
    mass: Mapped[int] = mapped_column(Integer)
    hair_color: Mapped[str] = mapped_column(String(20))
    eye_color: Mapped[str] = mapped_column(String(20))
    gender: Mapped[str] = mapped_column(String(20))
    skin_color: Mapped[str] = mapped_column(String(20))
    
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="character_table")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "skin_color": self.skin_color,
            # do not serialize the password, its a security breach
        }
    
class Planet(db.Model):
    __tablename__ = "planet"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    population: Mapped[int] = mapped_column(Integer)
    climate: Mapped[str] = mapped_column(String(50))
    terrain: Mapped[str] = mapped_column(String(50))
    diameter: Mapped[int] = mapped_column(Integer)
    rotation_period: Mapped[int] = mapped_column(Integer)
    orbitation_period: Mapped[int] = mapped_column(Integer)

    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="planet_table")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbitation_period": self.orbitation_period
            # do not serialize the password, its a security breach
        }