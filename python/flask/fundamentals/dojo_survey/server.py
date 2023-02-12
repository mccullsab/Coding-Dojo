from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "MBV!"

@app.route('/')
def form():
    return render_template("index.html")

@app.route('/process', methods = [ 'post' ])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/display')

@app.route('/display')
def display():
    print("display")
    return render_template("display.html")



if __name__=="__main__":
    app.run(debug=True, port = 5001)

