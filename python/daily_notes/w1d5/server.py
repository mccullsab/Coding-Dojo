from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Shhh no secrets og git!"


# RENDER ROUTE - PURPOSE IS TO RENDER A FORM
@app.route('/')
def form():
    return render_template("form.html")

#ACTION ROUTE --- CAPTURES INFOR FROM FORM -- NEVER RENDER ON AN POST/ACTION ROUTE (could cause duplicate chareges)
@app.route("/process", methods=[ 'post' ])
def process_form():
    print("form submitted")
    print(f"========\n\n {request.form} \n\n ========") #show me the information that the form is giving me, information submitted will be in browser unless more added, request form is the dictionart
    # print(f"dog_name: {request.form['name']}")
    # name = request.form['name']
    # age = request.form['age']

    # SESSION backpack, can be used anywhere
    session['name'] = request.form['name']
    session['age'] = request.form['age']
    session['breed'] = request.form['breed']
    session['store'] = request.form['store']

    return redirect("/display")

# RENDER ROUTE - PURPOSE IS TO RENDER DISPLAY
@app.route("/display")
def display():
    print("DISPLAY ROUTE")
    print(session['name'])

    return render_template("display.html")

# Clear session
@app.route("/clear")
def clear_session():
    session.clear()
    #del session['name'] to delete one thing
    return redirect("/display") # can only redirect to a get route

if __name__=="__main__":
    app.run(debug=True, port=5001)
