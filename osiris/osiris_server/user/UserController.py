from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from libs.ControllerResponse import ControllerResponse
from osiris_server.user.UserDAO import UserDAO


class UserController:

    @staticmethod
    def register_user(username, email, password, first_name, last_name) -> (ControllerResponse, str):
        user = User.objects.filter(email=email).first()
        if user is not None:
            return ControllerResponse.CLIENT_ERROR, 'Email address has already been taken.'
        user = authenticate(username=username, password=password)
        if user is None:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name)
            user.is_active = True
            user.save()
            return ControllerResponse.SUCCESS, 'User successfully registered.'
        else:
            return ControllerResponse.CLIENT_ERROR, 'User already exists.'

    @staticmethod
    def login(request, username, password) -> (ControllerResponse, str):
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return ControllerResponse.SUCCESS, 'Login successful.'
        else:
            return ControllerResponse.CLIENT_ERROR, 'Username or password is incorrect.'

    @staticmethod
    def logout(request):
        logout(request)

    @staticmethod
    def get(username) -> (int, dict):
        user = User.objects.filter(username=username).first()
        if not user:
            return ControllerResponse.CLIENT_ERROR, 'No user with this id exists.'
        user_dao = UserDAO.model_to_dao(user)
        return ControllerResponse.SUCCESS, user_dao.dict()

    @staticmethod
    def update(user, parsed_json):
        if 'email' in parsed_json and user.email != parsed_json['email']:
            user.email = parsed_json['email']
        if 'password' in parsed_json and user.password != parsed_json['password']:
            user.set_password(parsed_json['password'])
        if 'username' in parsed_json and user.username != parsed_json['username']:
            check_user = User.objects.filter(username=parsed_json['username']).first()
            if check_user:
                return ControllerResponse.CLIENT_ERROR, {'message': 'Username already taken.'}
            user.username = parsed_json['username']
        if 'first_name' in parsed_json and user.first_name != parsed_json['first_name']:
            user.first_name = parsed_json['first_name']
        if 'last_name' in parsed_json and user.last_name != parsed_json['last_name']:
            user.last_name = parsed_json['last_name']
        user.save()
        return ControllerResponse.SUCCESS, {'message': 'Info updated successfully.'}