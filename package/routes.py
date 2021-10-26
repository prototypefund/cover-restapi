import flask
from package import app


@app.route('/api/')
def hello():
    return flask.Response("302", status=302)
