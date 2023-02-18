from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.email_model import Email


@app.route ('/')
def index():
    return render_template("input.html")

@app.route('/process', methods = ['post'])
def create_email():
    new_email = Email.create(request.form)
    session['email'] = request.form['email']
    if not Email.validate(request.form):
        return redirect('/')
    return redirect('/display')

@app.route('/display')
def display():
    email_list = Email.get_all()
    return render_template("result.html", email_list = email_list)