from flask_restful import Resource
from flask import request
from flasgger import swag_from


class HelloWorld(Resource):
    @swag_from('hello.yml')
    def post(self):
        """Create new User entry in the users table
        """
        name = request.json.get('name')

        return {
            'message': f"Hello {name}"
        }, 200
