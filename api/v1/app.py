#!/usr/bin/python3

"""
Creating a handler for 404 errors
that returns a JSON-formatted
"""

from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(__name__)

# Registrar las rutas de la aplicación
app.register_blueprint(app_views)


# Manejador de errores 404
@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
