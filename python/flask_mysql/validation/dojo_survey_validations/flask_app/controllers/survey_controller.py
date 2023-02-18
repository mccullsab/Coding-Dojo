from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.survey_model import Survey


@app.route('/')
def form():
    return render_template("index.html")

@app.route('/process', methods = [ 'post' ])
def process():
    if not Survey.validate(request.form):
        return redirect('/')
    survey_id = Survey.create(request.form)
    return redirect(f'/display/{survey_id}')

@app.route('/display/<int:id>')
def display(id):
    data = {'id': id}
    this_survey = Survey.get_one(data)
    print("display")
    return render_template("display.html", this_survey = this_survey)

