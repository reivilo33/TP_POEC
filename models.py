# -*- coding: utf-8 -*-
# models.py
from datetime import datetime
from marshmallow_sqlalchemy import fields
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.ext.mutable import MutableDict

from config import db, ma

class Ingredient(db.Model):
    __tablename__ = "ingredients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    image = db.Column(db.String(32))
    prix = db.Column(db.Float)
    categorie = db.Column(db.String(32))
    unite = db.Column(db.String(32))

class IngredientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ingredient
        load_instance = True
        sqla_session = db.session

class Recette(db.Model):
    __tablename__ = "recettes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    temps = db.Column(db.String(32))
    image = db.Column(db.String(32))
    difficulte = db.Column(db.String(32))
    ingredients = db.Column(MutableDict.as_mutable(JSON), nullable=False, default=dict)
    instructions = db.Column(MutableDict.as_mutable(JSON), nullable=False, default=dict)

    @property
    def ingredients(self):
        """Retourne le contenu JSONB d'ingredients comme dictionnaire Python."""
        return self.ingredients or {}

    @property
    def instructions(self):
        """Retourne le contenu JSONB d'ingredients comme dictionnaire Python."""
        return self.instructions or {}

    @ingredients.setter
    def ingredients(self, value):
        """Met à jour le contenu JSONB à partir d'un dictionnaire."""
        if not isinstance(value, dict):
            raise ValueError("L'attribut 'ingredients' doit être un dictionnaire.")
        self.ingredients = value

    @instructions.setter
    def instructions(self, value):
        """Met à jour le contenu JSONB à partir d'un dictionnaire."""
        if not isinstance(value, dict):
            raise ValueError("L'attribut 'ingredients' doit être un dictionnaire.")
        self.instructions = value
    
class RecetteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recette
        load_instance = True
        sqla_session = db.session
        
ingredient_schema = IngredientSchema()
ingredients_schema = IngredientSchema(many=True)
recette_schema = RecetteSchema()
recettes_schema = RecetteSchema(many=True)