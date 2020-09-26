from flask import render_template, make_response
from flask_restful import Resource


class ExampleControllerViews(Resource):
    def get(self):
        view = render_template('index.html')
        return make_response(view)
