from flask import Blueprint

# Create a variable app_views which is an instance of Blueprint
# (url prefix must be /api/v1)
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all views from the package api.v1.views.index
# PEP8 will complain about wildcard imports, but it's necessary
# to avoid circular import errors
from api.v1.views.index import *
