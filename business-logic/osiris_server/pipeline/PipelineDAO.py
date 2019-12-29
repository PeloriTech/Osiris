from osiris_server.pipeline.PipelineModel import Pipeline
from osiris_server.user.UserDAO import UserDAO


class PipelineDAO:

    def __init__(self, id: str, owner: UserDAO, input_stream: str, input_type: str,
                 stream_processor: str, videostream_port: int, remote_address: str,
                 websocket_port: int, pid):
        self.id = id
        self.owner = owner
        self.input_stream = input_stream
        self.input_type = input_type
        self.stream_processor = stream_processor
        self.videostream_port = videostream_port
        self.websocket_port = websocket_port
        self.remote_address = remote_address,
        self.pid = pid

    @staticmethod
    def model_to_dao(pipeline: Pipeline):
        owner = UserDAO.model_to_dao(pipeline.owner)
        dao = PipelineDAO(
            id=pipeline.id,
            owner=owner,
            input_stream=pipeline.input_stream,
            input_type=pipeline.input_type,
            stream_processor=pipeline.stream_processor,
            videostream_port=pipeline.videostream_port,
            websocket_port=pipeline.websocket_port,
            remote_address=pipeline.remote_address,
            pid=pipeline.pid
        )
        return dao

    @staticmethod
    def dao_to_model(dao):
        pass

    def dict(self):
        return {
            "id": self.id,
            "owner": self.owner.dict(),
            "input_stream": self.input_stream,
            "input_type": self.input_type,
            "stream_processor": self.stream_processor,
            "remote_address": self.remote_address[0],
            "videostream_port": self.videostream_port,
            "websocket_port": self.websocket_port,
            "pid": self.pid
        }
