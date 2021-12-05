from flask import Flask, jsonify

app = Flask(__name__)

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
