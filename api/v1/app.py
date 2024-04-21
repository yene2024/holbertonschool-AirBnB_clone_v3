#!/usr/bin/python3

"""
Creating a handler for 404 errors
that returns a JSON-formatted
"""

from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """ gives json 404 error """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    """ Connects to host """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
