from osiris.SimplePipeline import SimplePipeline
from osiris.Processor import YoloV3Processor
from osiris.VideoSource import USBVideoSource
from osiris.VideoOutput import CV2ImshowOutput
from osiris.DataSink import ConsoleDataSink

usbCamera1 = USBVideoSource()
yolov3processor = YoloV3Processor()
console_output = ConsoleDataSink()
cv2Output = CV2ImshowOutput()

pipeline = SimplePipeline(usbCamera1, yolov3processor, console_output, cv2Output)
pipeline.start(attached=True)
