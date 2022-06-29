from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'h23l4nvkl2390lknwe23ngfklwef'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app