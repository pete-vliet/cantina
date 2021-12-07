from flask import jsonify
from api import app
from api.models import CollectionItem
from api.db import db_session

@app.route("/home")
def index():
    nas = CollectionItem.query.all()[0]
    dashboard_payload = {
        'name': 'joe six-pack',
        'collection': [{
            'title': nas.title,
            'main_artist': nas.main_artist,
            'genre': nas.genre,
            'image_url': nas.image_url,
        }]
    }

    return jsonify(dashboard_payload)

    # [
    #     {
    #         'title': 'Harvest',
    #         'main_artist': 'Neil Young',
    #         'genre': 'rock',
    #         'image_url': 'https://upload.wikimedia.org/wikipedia/en/9/9b/NeilYoungHarvestalbumcover.jpg'
    #     },
    #     {
    #         'title': 'Purple Rain',
    #         'main_artist': 'Prince',
    #         'genre': 'rock',
    #         'image_url': 'https://upload.wikimedia.org/wikipedia/en/9/9c/Princepurplerain.jpg'
    #     },
    #     {
    #         'title': 'Illmatic',
    #         'main_artist': 'Nas',
    #         'genre': 'hip-hop/rap',
    #         'image_url': 'https://upload.wikimedia.org/wikipedia/en/2/27/IllmaticNas.jpg',
    #     }
    # ]
