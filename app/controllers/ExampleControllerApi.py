from flask_restful import Resource

from app import response


class ExampleControllerApi(Resource):
    def get(self):
        return response.ok('', 'ok!')
