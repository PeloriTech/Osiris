
import cv2
from pydarknet import Detector, Image
from .Processor import Processor
import logging

logger = logging.getLogger(__name__)


class YoloV3Processor(Processor):


    def __init__(self):
        Processor.__init__(self)
        self.net = None


    def start(self):
        logger.info("Starting YoloV3 Processor")
        self.net = Detector(bytes("cfg/yolov3.cfg", encoding="utf-8"),
                            bytes("weights/yolov3.weights", encoding="utf-8")
                            , 0, bytes("cfg/coco.data", encoding="utf-8"))
        self.status = True

    def process_frame(self, frame, output_annotated:bool=True):


        if self.status:

            frame = cv2.resize(frame, (800, 600))
            dark_frame = Image(frame)
            results = self.net.detect(dark_frame)
            del dark_frame

            for category, score, bounds in results:
                    x, y, w, h = bounds
                    if output_annotated:
                        cv2.rectangle(frame, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), (255, 0, 0))
                        cv2.putText(frame, str(category.decode("utf-8")), (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 1,
                                    (255, 255, 0))

            return frame, results
        else:
            raise ValueError("The processor is not started")



    def stop(self):
        logger.info("Stopping processor YoloV3")
        del self.net
        self.net = None
        self.status = False


    def check_health(self):
        pass