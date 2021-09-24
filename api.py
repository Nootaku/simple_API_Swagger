from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flasgger import Swagger

# Internal imports
from resources.hello import HelloWorld
from resources.records import Records


def create_app():
    """Application Factory for our app.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config['SWAGGER'] = {
        'title': 'Flasgger & Flask RESTful',
        'version': '0.1.0',
        'description': 'Testing a Swagger UI with a Flask Restful API',
        'uiversion': 3
    }
    CORS(app)
    api = Api(app)
    swagger = Swagger(app)

    if app.config['ENV'] == "development":
        app.config.from_object('config.DevelopmentConfig')
    elif app.config['ENV'] == "production":
        app.config.from_object('config.ProductionConfig')

    api.add_resource(HelloWorld, '/hello')
    api.add_resource(Records, '/records')

    return app


if __name__ == '__main__':
    create_app()
