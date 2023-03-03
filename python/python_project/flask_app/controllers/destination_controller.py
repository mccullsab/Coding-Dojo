from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.destination_model import Destination
from flask_app.models.user_model import User
from flask_app.models.blog_model import Blog

# from flask_app.controllers import blog_controller
from flask import flash

# -------------Render - Create a Destination-------------

@app.route('/destination/create')
def new_destination():
    data = {
        'id': session['user_id']
    }
    logged_user = User.get_one(data)
    return render_template("trip_landingpage.html", logged_user=logged_user)

# ---------------Create a Destination-------------------

@app.route('/create/destination', methods=["POST"])
def create_destination():
    print(request.form)
    if not Destination.validate(request.form):
        return redirect('/destination/create')
    destination_data = {
        **request.form,
        'user_id' : session['user_id']
        }
    destination_id = Destination.create(destination_data)
    return redirect(f'/blog/create/{destination_id}')


#---------Get all destination blogs----------
@app.route('/destination/<int:id>')
def get_one(id):
    blog_instances = Destination.get_all_blogs({'id':id})
    return render_template('trip_show.html', blog_instances = blog_instances)