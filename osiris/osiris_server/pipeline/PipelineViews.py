from rest_framework.decorators import api_view
from django.http import HttpResponse
import json
from libs.utils import validate_body
from libs.ControllerResponse import ControllerResponse
from osiris_server.pipeline.PipelineViewSchemas import PipelineViewSchemas
from osiris_server.pipeline.PipelineController import PipelineController
from django.contrib.auth.decorators import login_required
from libs.utils import get_client_ip


class PipelineViews:

    @staticmethod
    @login_required
    @api_view(['POST'])
    @validate_body(PipelineViewSchemas.launch)
    def launch(request) -> HttpResponse:
        body = request.data
        remote_address = get_client_ip(request)
        con_resp, resp_dict = PipelineController.launch(remote_address,
                                                        request.user,
                                                        body['input_stream'],
                                                        body['input_type'],
                                                        body['stream_processor'])
        status = ControllerResponse.controller_response_to_http_status(con_resp)
        resp_json = json.dumps(resp_dict)
        return HttpResponse(resp_json, content_type="application/json", status=status)

    @staticmethod
    def get_available_pipelines(request):
        pass

    @staticmethod
    def create_new_pipeline(request):
        pass

    @staticmethod
    @login_required
    @api_view(['POST'])
    @validate_body(PipelineViewSchemas.start)
    def start(request) -> HttpResponse:
        body = request.data
        con_resp, resp_dict = PipelineController.start(body['id'])
        status = ControllerResponse.controller_response_to_http_status(con_resp)
        resp_json = json.dumps(resp_dict)
        return HttpResponse(resp_json, content_type="application/json", status=status)

    @staticmethod
    @login_required
    @api_view(['GET'])
    def list(request) -> HttpResponse:
        con_resp, resp_dict = PipelineController.list(request.user)
        status = ControllerResponse.controller_response_to_http_status(con_resp)
        resp_json = json.dumps(resp_dict)
        return HttpResponse(resp_json, content_type="application/json", status=status)

    @staticmethod
    @login_required
    @api_view(['POST'])
    @validate_body(PipelineViewSchemas.stop)
    def stop(request) -> HttpResponse:
        body = request.data
        con_resp, resp_dict = PipelineController.stop(body['id'])
        status = ControllerResponse.controller_response_to_http_status(con_resp)
        resp_json = json.dumps(resp_dict)
        return HttpResponse(resp_json, content_type="application/json", status=status)

    @staticmethod
    @login_required
    @api_view(['POST'])
    @validate_body(PipelineViewSchemas.terminate)
    def terminate(request) -> HttpResponse:
        body = request.data
        con_resp, resp_dict = PipelineController.terminate(body['id'])
        status = ControllerResponse.controller_response_to_http_status(con_resp)
        resp_json = json.dumps(resp_dict)
        return HttpResponse(resp_json, content_type="application/json", status=status)
