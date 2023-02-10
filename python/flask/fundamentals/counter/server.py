from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "Shhh no secrets on git!"


@app.route('/')
def visits():
    if not 'times' in session:
        session['times'] = 1
    else:
        session['times'] +=1

    return render_template("index.html")

@app.route("/destroy")
def destroy():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)