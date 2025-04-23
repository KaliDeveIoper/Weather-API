from flask import Flask
from backend.routes import consultarClima
from dotenv import load_dotenv
import os
from backend.app.cache import cache


def create_app():
    load_dotenv()
    app=Flask(__name__,template_folder='../templates')
    cache.init_app(app)
    
    app.register_blueprint(consultarClima)

    return app


