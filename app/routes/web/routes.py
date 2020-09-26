from flask_restful import Api

from app import app
from app.controllers import ExampleControllerViews

web = Api(app)
web.add_resource(ExampleControllerViews.ExampleControllerViews, '/')
