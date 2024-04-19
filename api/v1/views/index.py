#!/usr/bin/python3

"""
Creating an endpoint that retrieves
the number of each objects by type
"""
from flask import jsonify
from flask import Blueprint
from models import storage

app_views = Blueprint('app_views', __name__)


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieve the number of each object type."""
    counts = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(counts)
