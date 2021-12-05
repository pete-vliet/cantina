import os

from flask import Flask, jsonify


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'api.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/api")
    def hello_world():
        dashboard_payload = {
            'name': 'joe six-pack',
            'collection': [
                {
                    'title': 'Harvest',
                    'main_artist': 'Neil Young',
                    'genre': 'rock',
                    'image_url': 'https://upload.wikimedia.org/wikipedia/en/9/9b/NeilYoungHarvestalbumcover.jpg'
                },
                {
                    'title': 'Purple Rain',
                    'main_artist': 'Prince',
                    'genre': 'rock',
                    'image_url': 'https://upload.wikimedia.org/wikipedia/en/9/9c/Princepurplerain.jpg'
                },
                {
                    'title': 'Illmatic',
                    'main_artist': 'Nas',
                    'genre': 'hip-hop/rap',
                    'image_url': 'https://upload.wikimedia.org/wikipedia/en/2/27/IllmaticNas.jpg',
                }
            ]
        }
        return jsonify(dashboard_payload)

    from . import db
    db.init_app(app)

    return app
