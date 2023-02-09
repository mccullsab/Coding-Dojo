from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a variable, run an instance of flask in this file (name)


#"local host 1337, execute this function"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/cool')
def success():
    return 'succes'

@app.route('/cool/<name>')
def var_info(name):
    return f"<h1>succes {name}</h1>"

@app.route('/cool/<someVar>/<int:times>')
def varmore_info(someVar, times):
    return f"<p>succes {someVar}</p>" * times

@app.route('/hello_temp/<string:banana>/<int:num>')
def cooler(banana, num):
    return render_template("hello.html", banana = banana, num = num)


#cant have the same function name in 2 diff routes, if you have the same route it will only return the furst one


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=1337)    # Run the app in debug mode. change the port from 5000 to 1337 by changing the port