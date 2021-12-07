import flask
import os
from flask import send_from_directory

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    return '<html lang="en"> <head><meta charset="UTF-8"><title>FlaskApp</title></head><body> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Heroku_logo.svg/2560px-Heroku_logo.svg.png" width="1020" height="285" alt="alternatetext"> <h1>BULUT BİLİŞİM(CLOUD COMPUTING)</h1><h2>HerokuAPP!</h2><a href="https://heroku.com/">               link->heroku</a></body></html>'

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()