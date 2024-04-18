#!/usr/bin/python3

from flask import jsonify
from . import app_views


# Create a route /status on the object app_views
@app_views.route('/status', methods=['GET'])
def status():
    """Return the status of the API."""
    return jsonify({"status": "OK"})
