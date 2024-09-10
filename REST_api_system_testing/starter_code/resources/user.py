from flask_restful import Resource, reqparse
from Automated_Testing.REST_api_system_testing.starter_code.models.user import UserModel


class UserRegister(Resource):
    """
    This resource allows users to register by sending a
    POST request with their username and password.
    """
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    def post(self):