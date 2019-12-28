import cv2
from .VideoSource import VideoSource


class USBVideoSource(VideoSource):

    def __init__(self, usb_path: str = None):
        VideoSource.__init__(self)

        self.video_device_name = usb_path

    def start(self):
        self.status = True
        self.createVideoPipe()

    def stop(self):
        pass
        #TODO


    def createVideoPipe(self):

        self.videoPipe = cv2.VideoCapture(self._getAppSourceString(), cv2.CAP_GSTREAMER)

    def _getAppSourceString(self):

        if self.video_device_name is not None:

            return "v4l2src device={} ! queue leaky=downstream max-size-time=1 ! videoconvert ! appsink".format(
                self.video_device_name)
        else:

            return "v4l2src ! queue leaky=downstream max-size-time=1 ! videoconvert ! appsink"

    def grab_frame(self):

        if self.status:
            ret, frame = self.videoPipe.read()
            return ret, frame
        else:
            raise ValueError("Video source not started")
