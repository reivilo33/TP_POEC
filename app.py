# -*- coding: utf-8 -*-
# app.py

from flask import render_template, request, redirect, url_for, abort
import config
from models import Recette

app = config.app
db = config.db

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/recettes", methods=["GET"])
def recettes_index():
    recettes = Recette.query.all()
    return render_template("index.html", recettes=recettes)


@app.route("/recettes/<int:id>", methods=["GET"])
def recette_show(id):
    recette = Recette.query.get_or_404(id)
    return render_template("show.html", recette=recette)


@app.route("/recettes", methods=["POST"])
def recette_create():
    recette = Recette(
        nom=request.form.get("nom"),
        temps=request.form.get("temps"),
        image=request.form.get("image_link"),
        difficulte=request.form.get("difficulte"),
        ingredients=request.form.get("ingredients"),
        instructions=request.form.get("instructions"),
    )

    db.session.add(recette)
    db.session.commit()

    return redirect(url_for("recette_show", id=recette.id))


@app.route("/recettes/<int:id>/delete", methods=["POST"])
def recette_delete(id):
    recette = Recette.query.get_or_404(id)
    db.session.delete(recette)
    db.session.commit()

    return redirect(url_for("recettes_index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)