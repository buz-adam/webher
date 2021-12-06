import flask
import os
from flask import send_from_directory

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    return '<html lang="en"> <head><meta charset="UTF-8"><title>FlaskApp</title></head><body><h1>Hello World!</h1><h2>FlaskApp!</h2></body></html>'

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()