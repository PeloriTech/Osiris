



class VideoSource:


    def __init__(self):
        self.status = False # is the video source active?
        # can multiple processors use the same video source? ip cameras do support multiple clients


    def grab_frame(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass