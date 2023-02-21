from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)

#RENDER LOGIN/REGISTER
@app.route('/')
def register_users():
    # session = session['first_name']
    return render_template("register.html")

#PROCESS FORM AND VALIDATE
@app.route('/process', methods = ['POST'])
def user_capture():
    if not User.validate(request.form):
        return redirect('/')
    
    #1. hash pw
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    #2. get data dict with new hashed pass to create user
    data = {
        **request.form,
        'password' : pw_hash
    }
    #3. pass to query
    user_id = User.create(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

#RENDER DASBOARD
@app.route('/dashboard')
def user_display():
    if 'user_id' not in session:
        return redirect ('/')
    data = {
        'id' : session['user_id']
    }
    logged_user = User.get_one(data)
    return render_template("dashboard.html", logged_user=logged_user)

#LOGIN USER - ROUTE
@app.route("/users/login", methods = ['POST'])
def user_login():
    data = {
        'email': request.form['email']
    }
    user_in_db = User.get_by_email(data)
    
    #check email
    if not user_in_db:
        flash("invalid credentials")
        return redirect("/")
    
    #check the pw
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    
    #if all is good
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

#LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')




