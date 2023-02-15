from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "MBV!"

@app.route('/')
def home():
    # if I haven't already came up with a random number, generate one
    if "num" not in session:
        session['num'] = random.randint(1,10)
    return render_template("index.html")

#ACTION ROUTE --- CAPTURES INFOR FROM FORM -- NEVER RENDER ON AN POST/ACTION ROUTE (could cause duplicate chareges)
@app.route("/process", methods=[ 'post' ])
def process_guess():
    session['guess'] = int(request.form['guess'])
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

# #RENDER ROUTE
# @app.route("/display")
# def display():
#     print(session['guess'])
#     return render_template("display.html")



#type number, create a session number, check number against what is stored in the system
# if the number is less than the stored number (hidden on html? or is the number in the route and on the page in jinja?) 
#   then create a div with the lower message on the html page with the if them in curly brackets



if __name__=="__main__":
    app.run(debug=True, port = 5001)