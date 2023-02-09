from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a variable, run an instance of flask in this file (name)


@app.route('/play')
def level_one():
    return render_template("level_one.html")

@app.route('/play/<int:num>')
def level_two(num):
    return render_template("level_two.html", num=num)

@app.route('/play/<int:num>/<string:color>')
def level_three(num, color):
    return render_template("level_three.html", num=num, color=color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode. change the port from 5000 to 1337 by changing the port