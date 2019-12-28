from enum import Enum


class ControllerResponse(Enum):

    CLIENT_ERROR = 1
    SERVER_ERROR = 2
    SUCCESS = 3

    @staticmethod
    def controller_response_to_http_status(cont_response):
        if cont_response == ControllerResponse.CLIENT_ERROR:
            return 400
        elif cont_response == ControllerResponse.SERVER_ERROR:
            return 500
        elif cont_response == ControllerResponse.SUCCESS:
            return 200
