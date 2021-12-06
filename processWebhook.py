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
    return '<html lang="en"> <head><meta charset="UTF-8"><title>FlaskApp</title></head><body> <img src="https://ichi.pro/assets/images/max/724/0*hVrbNMq2F7OkXVnE" alt="alternatetext">  <h1>Merhaba DÜNYA!</h1><h2>HerokuAPP!</h2></body></html>'

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()