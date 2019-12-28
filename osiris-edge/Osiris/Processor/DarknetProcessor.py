from Osiris.Processor.BaseOsirisProcessor import BaseOsirisProcessor
from pydarknet import Detector, Image


class DarknetProcessor(BaseOsirisProcessor):

    def __init__(self):
        net = Detector(bytes("cfg/yolov3.cfg", encoding="utf-8"), bytes("weights/yolov3.weights", encoding="utf-8"), 0,
                        bytes("cfg/coco.data", encoding="utf-8"))

    def annotate(self, frame, results):
        for cat, score, bounds in results:
            x, y, w, h = bounds
            cv2.rectangle(frame, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), (255, 0, 0))
            cv2.putText(frame, str(cat.decode("utf-8")), (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (255, 255, 0))