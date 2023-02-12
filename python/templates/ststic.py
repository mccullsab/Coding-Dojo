from flask import Flask, session
app = Flask(__name__)
app.secret_key = "MBV!"


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__=="__main__":
    app.run(debug=True)

