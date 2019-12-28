from .VideoSourceTemplate import VideoSourceTemplate
from .VideoSource import VideoSource
from .IPCameraVideoSource import IPCameraVideoSource
from .USBVideoSource import USBVideoSource


class VideoSourceFactory:


    @staticmethod
    def create_input_source(template: VideoSourceTemplate):

        if template.type == "USBVideoSource":
            return VideoSourceFactory._create_USBVideoSource(template.data["path"])
        elif template.type == "IPCameraVideoSource":
            return VideoSourceFactory._create_IPCameraVideoSource(template.data["host"], template.data["username"],
                                                    template.data["password"])
        else:
            raise ValueError("Video Source " + str(template.type) + " is not supported")

    @staticmethod
    def _create_USBVideoSource(path: str) -> USBVideoSource:
        return USBVideoSource(path)

    @staticmethod
    def _create_IPCameraVideoSource(host, username, password) -> IPCameraVideoSource:
        return IPCameraVideoSource(host, username, password)
