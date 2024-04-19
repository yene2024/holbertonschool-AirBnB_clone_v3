#!/usr/bin/python3

"""
return the status
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

# Register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Close the database connection when the app context ends.

    Args:
        exception: The exception, if any, that occurred during the app context.
    """
    storage.close()


if __name__ == "__main__":
    """
    Run the Flask server.
    """
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', 5000)),
            threaded=True)
