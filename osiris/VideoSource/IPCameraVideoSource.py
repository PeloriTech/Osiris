from .VideoSource import VideoSource


class IPCameraVideoSource(VideoSource):

    def __init__(self, host, username, password):
        VideoSource.__init__(self)
        self.host = host
        self.username = username
        self.password = password


    def start(self):
        pass

    def stop(self):
        pass
