from flask_app import app
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

from flask import render_template, request, redirect

#Create ninja render
@app.route('/ninja/new')
def new():
    all_dojos = Dojo.get_all()
    return render_template('ninja_create.html', all_dojos = all_dojos)

#Create ninja post
@app.route('/ninja/create', methods = ['POST'])
def create():
    new_ninja = Ninja.create(request.form)
    return redirect('/ninja/new')