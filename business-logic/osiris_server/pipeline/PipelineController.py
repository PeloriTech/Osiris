import psutil
from django.contrib.auth.models import User
from libs.ControllerResponse import ControllerResponse
from osiris_server.pipeline.PipelineModel import Pipeline
from osiris_server.pipeline.PipelineDAO import PipelineDAO

from pipeline_manager.PipelineManager import PipelineManager


class PipelineController:

    @staticmethod
    def launch(remote_address, user: User, input_stream: str, input_type: str,
               stream_processor: str) -> (ControllerResponse, dict):
        if stream_processor not in PipelineManager.image_processors.keys():
            return ControllerResponse.CLIENT_ERROR, "Cannot find model \"{}\".".format(stream_processor)
        videostream_port = PipelineController.get_available_port()
        websocket_port = PipelineController.get_available_port(videostream_port)
        pipeline = Pipeline(owner=user, input_stream=input_stream, stream_processor=stream_processor,
                            input_type=input_type, videostream_port=videostream_port,
                            websocket_port=websocket_port, remote_address=remote_address)
        pipeline_dao = PipelineDAO.model_to_dao(pipeline)
        pid = PipelineManager.start(pipeline_dao)
        pipeline.pid = pid
        pipeline.save()
        pipeline_dao = PipelineDAO.model_to_dao(pipeline)
        response_dict = pipeline_dao.dict()
        response_dict['status'] = PipelineController.get_status(pid)
        return ControllerResponse.SUCCESS, response_dict

    @staticmethod
    def get_available_pipeline_templates():
        pass


    @staticmethod
    def start(pipeline_id: str):
        pipeline = Pipeline.objects.filter(id=pipeline_id).first()
        if not pipeline:
            return ControllerResponse.CLIENT_ERROR, 'SimplePipeline does not exist.'
        pipeline_dao = PipelineDAO.model_to_dao(pipeline)
        pid = PipelineManager.start(pipeline_dao)
        pipeline.pid = pid
        pipeline.save()
        pipeline_dao = PipelineDAO.model_to_dao(pipeline)
        response_dict = pipeline_dao.dict()
        response_dict['status'] = PipelineController.get_status(pid)
        return ControllerResponse.SUCCESS, response_dict

    @staticmethod
    def stop(pipeline_id: str):
        pipeline = Pipeline.objects.filter(id=pipeline_id).first()
        if not pipeline:
            return ControllerResponse.CLIENT_ERROR, {'message': 'SimplePipeline does not exist.'}
        if psutil.pid_exists(pipeline.pid):
            p = psutil.Process(pipeline.pid)
            if 'python' in p.name():
                p.terminate()
                return ControllerResponse.SUCCESS, {'message': 'SimplePipeline successfully stopped.'}
        return ControllerResponse.CLIENT_ERROR, {'message': 'SimplePipeline was not running.'}

    @staticmethod
    def terminate(pipeline_id: str):
        pipeline = Pipeline.objects.filter(id=pipeline_id).first()
        if not pipeline:
            return ControllerResponse.CLIENT_ERROR, {'message': 'SimplePipeline does not exist.'}
        pipeline.delete()
        if psutil.pid_exists(pipeline.pid):
            p = psutil.Process(pipeline.pid)
            if 'python' in p.name():
                p.terminate()
                return ControllerResponse.SUCCESS, {'message': 'SimplePipeline stopped and successfully terminated.'}
        return ControllerResponse.SUCCESS, {'message': 'SimplePipeline successfully terminated.'}

    @staticmethod
    def list(user: User):
        pipelines = Pipeline.objects.filter(owner=user).all()
        pipeline_list = []
        for pipeline in pipelines:
            pipeline_dao = PipelineDAO.model_to_dao(pipeline)
            response_dict = pipeline_dao.dict()
            response_dict['status'] = PipelineController.get_status(pipeline_dao.pid)
            pipeline_list += [response_dict]
        return ControllerResponse.SUCCESS, pipeline_list

    @staticmethod
    def get_available_port(other_than_this_one=-1):
        available_port = 5000
        ports = list(x[0] for x in Pipeline.objects.values_list('videostream_port'))
        ports += list(x[0] for x in Pipeline.objects.values_list('websocket_port'))
        ports += [other_than_this_one]
        while available_port in ports:
            available_port += 1
        return available_port

    @staticmethod
    def get_status(pid):
        if psutil.pid_exists(pid):
            p = psutil.Process(pid)
            if 'python' in p.name() and p.status() is not psutil.STATUS_ZOMBIE:
                return "RUNNING"
        return "STOPPED"
