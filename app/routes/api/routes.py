from flask_restful import Api

from app import app
from app.controllers import ExampleControllerApi

api = Api(app, prefix="/api")
api.add_resource(ExampleControllerApi.ExampleControllerApi, '/')
