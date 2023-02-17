from flask_app import app
from flask_app.models.dojo_model import Dojo

from flask import render_template, request, redirect

#Create Render
@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    return render_template('dojo_create.html', all_dojos = all_dojos)

#Create Capture
@app.route('/dojo/new', methods = ['POST'])
def create_dojo():
    new_dojo = Dojo.create(request.form)
    return redirect('/')

#Display Dojo's Ninjas (Get One)
@app.route('/dojo/<int:id>/display')
def get_one(id):
    one_dojo = Dojo.get_one({'id': id})
    return render_template('dojo_display.html', one_dojo = one_dojo)