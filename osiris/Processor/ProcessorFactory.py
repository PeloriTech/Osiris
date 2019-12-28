from .Processor import Processor
from .ProcessorTemplate import ProcessorTemplate
from .YoloV3Processor import YoloV3Processor
from .FaceDetectionProcessor import FaceDetectionProcessor

class ProcessorFactory:

    @staticmethod
    def create_processor(template:ProcessorTemplate):

        if template.type == "YoloV3":
            return YoloV3Processor()
        elif template.type == "FaceRecognition":
            return FaceDetectionProcessor()
        else:
            raise ValueError("Unknown type " + str(template.type))


