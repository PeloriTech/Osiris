import cv2
from multiprocessing import Process
from osiris_server.pipeline.PipelineDAO import PipelineDAO
from pipeline_manager.VideoProcessor.SimpleObjectDetection.SimpleObjectDetectionProcessor import SimpleObjectDetectionProcessor
from pipeline_manager.VideoProcessor.BaseProcessor import BaseProcessor


class PipelineManager:

    net = None

    input_pipelines = {
        'rtsp': 'rtspsrc latency=0 location={} ! queue ! application/x-rtp,\
         encoding-name=H264,payload=96 !\
         rtph264depay ! avdec_h264 ! videoconvert ! queue leaky=downstream ! appsink',

        'test': 'videotestsrc ! videoconvert ! appsink',

        'usb': 'v4l2src ! videoconvert ! appsink'
    }

    image_processors = {
        'no_model': BaseProcessor,
        'simple_object_detection_model': SimpleObjectDetectionProcessor
    }

    @staticmethod
    def send(osiris_pipeline: PipelineDAO):

        if osiris_pipeline.input_type == 'test':
            gstreamer_input_pipeline = PipelineManager.input_pipelines[osiris_pipeline.input_type]
        else:
            gstreamer_input_pipeline = PipelineManager.input_pipelines[osiris_pipeline.input_type].format(
                osiris_pipeline.input_stream)
        print("PIPELINE: {}".format(gstreamer_input_pipeline))
        cap_send = cv2.VideoCapture(gstreamer_input_pipeline, cv2.CAP_GSTREAMER)

        gstreamer_output_pipeline = 'appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500\
         speed-preset=superfast ! rtph264pay config-interval=1 pt=48 mtu=1000 ! \
          udpsink host={} port={}'.format(
            osiris_pipeline.remote_address[0], osiris_pipeline.videostream_port)
        print("OUTPUT_STREAM: {}".format(gstreamer_output_pipeline))
        out_send = cv2.VideoWriter(gstreamer_output_pipeline, cv2.CAP_GSTREAMER, 0, 30, (640, 480), True)

        print("capsend: ", cap_send.isOpened())
        print("outsend: ", out_send.isOpened())

        if not cap_send.isOpened():
            print('VideoCapture or VideoWriter not opened')
            exit(0)

        processor: BaseProcessor = PipelineManager.image_processors[osiris_pipeline.stream_processor]()

        processor.start(cap_send=cap_send, out_send=out_send, websocket_port=osiris_pipeline.websocket_port)

        cap_send.release()
        out_send.release()

    @staticmethod
    def start(osiris_pipeline):
        process = Process(target=PipelineManager.send, args=(osiris_pipeline,))
        osiris_pipeline.process = process
        process.start()
        return process.pid

