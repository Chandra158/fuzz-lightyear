from functools import lru_cache

from flask import Flask


@lru_cache(maxsize=1)
def get_current_application():
    return create_app()


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug

    # Make trailing slashes in routes redundant.
    app.url_map.strict_slashes = False

    return app
