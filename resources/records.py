from flask_restful import Resource
from flask import request
from flasgger import swag_from


class Records(Resource):
    @swag_from('records.yml')
    def get(self):
        name = request.args.get('name')

        return {
            'message': f"Get your name:  {name}"
        }, 200

    @swag_from('records.yml')
    def post(self):
        name = request.args.get('name')

        return {
            'message': f"Post your name:  {name}"
        }, 201
