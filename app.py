# -*- coding: utf-8 -*-
# app.py
from flask import render_template, jsonify, request # Remove: import Flask
import config
from models import Recette

app = config.app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/recettes", methods=['GET'])
def recettes():
    recettes = Recette.query.all()
    return render_template("index.html", recettes=recettes)

@app.route("/recettes/<id>", methods=['GET'])
def recette(id):
    recette = Recette.query.get(id)
    return render_template("show.html", recette=recette)

@app.route("/recettes", methods=['POST'])
def new_recette():
    recette = Recette(
        nom = request.form.get("nom"),
        temps = request.form.get("temps"),
        image = request.form.get("image_link"),
        difficulte = request.form.get("difficulte"),
        ingredients = request.form.get("ingredients"),
        instructions = request.form.get("instructions")
    )
    db.session.add(recette)
    db.session.commit()

@app.route("/recettes/<id>")
def del_recette(id):
    recette = Recette.query.get(id)
    db.session.delete(recette)
    db.session.commit()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)