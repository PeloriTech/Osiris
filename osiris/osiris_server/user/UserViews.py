from rest_framework.decorators import api_view
from django.http import HttpResponse
import json
from libs.utils import validate_body
from libs.ControllerResponse import ControllerResponse
from osiris_server.user.UserViewSchemas import UserViewSchemas
from osiris_server.user.UserController import UserController
from django.contrib.auth.decorators import login_required


class UserViews:

    @staticmethod
    @api_view(['POST'])
    @validate_body(UserViewSchemas.register_user)
    def register_user(request) -> HttpResponse:
        body = request.data
        username = body['username']
        password = body['password']
        email = body['email']
        first_name = body['first_name']
        last_name = body['last_name']
        status, message = UserController.register_user(username, email, password,
                                                       first_name, last_name)
        status = ControllerResponse.controller_response_to_http_status(status)
        response_data = {'message': message}
        response_json = json.dumps(response_data, indent=4, separators=(',', ': '))
        return HttpResponse(response_json, content_type="application/json", status=status)

    @staticmethod
    @api_view(['POST'])
    @validate_body(UserViewSchemas.login)
    def login(request) -> HttpResponse:
        body = request.data
        status, message = UserController.login(request, body['username'], body['password'])
        status = ControllerResponse.controller_response_to_http_status(status)
        response_json = json.dumps(message)
        return HttpResponse(response_json, content_type="application/json", status=status)

    @staticmethod
    @login_required
    @api_view(['GET'])
    def get(request):
        con_resp, user_dict = UserController.get(request.user.username)
        response_json = json.dumps(user_dict)
        status = ControllerResponse.controller_response_to_http_status(con_resp)
        return HttpResponse(response_json, content_type="application/json", status=status)

    @staticmethod
    @login_required
    @api_view(['POST'])
    def info(request):
        body = request.data
        con_resp, response_dict = UserController.get(body['username'])
        response_json = json.dumps(response_dict)
        status = ControllerResponse.controller_response_to_http_status(con_resp)
        return HttpResponse(response_json, content_type="application/json", status=status)

    @staticmethod
    @login_required
    @api_view(['POST'])
    @validate_body(UserViewSchemas.update_user_info)
    def update(request):
        parsed_json = request.data
        con_resp, data = UserController.update(request.user, parsed_json)
        status = ControllerResponse.controller_response_to_http_status(con_resp)
        return HttpResponse(json.dumps(data), content_type="application/json", status=status)

    @staticmethod
    @login_required
    @api_view(['GET'])
    def is_logged_in(request):
        if request.user.is_active:
            response_json = json.dumps(True)
            return HttpResponse(response_json, content_type="application/json", status=200)
        else:
            response_json = json.dumps(False)
            return HttpResponse(response_json, content_type="application/json", status=200)

