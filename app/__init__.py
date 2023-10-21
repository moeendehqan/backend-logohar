

from flask import Flask
from flask_cors import CORS
from mongoengine import connect
from config import config
from app.resources import api

def create_app(environment='default'):
    app = Flask(__name__)
    CORS(app)
    api.init_app(app)

    app.config['MONGODB_SETTINGS'] = config[environment].MONGODB_SETTINGS
    connect(**app.config['MONGODB_SETTINGS'])

    return app
