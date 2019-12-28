

class VideoOutput:

    def __init__(self):
        self.state = False #if it is a gstreamer output we need to check whether the process is up!

    def start(self):
        pass

    def stop(self):
        pass

    def push_frame(self, frame):
        pass