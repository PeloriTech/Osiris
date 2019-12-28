import threading

from osiris.VideoSource import VideoSource
from osiris.Processor import Processor
from osiris.DataSink import DataSink
from osiris.VideoOutput import VideoOutput


class SimplePipeline:

    def __init__(self, video_input: VideoSource, processor: Processor, datasink:DataSink, video_output:VideoOutput):
        self.VideoInput = video_input
        self.Processor = processor
        self.DataSink = datasink
        self.VideoOutput = video_output

    def start(self, attached=False):
        """
        Go through all the elements and initialize them! Afterwards start the pipeline tick
        :return:
        """

        self.VideoInput.start()
        self.DataSink.start()
        self.VideoOutput.start()
        self.Processor.start()

        self.status = True

        if attached:
            self._tick_thread()
        else:
            tick_thread = threading.Thread(target=self._tick_thread)
            tick_thread.daemon = True
            tick_thread.start()

    def _tick_thread(self):
        while self.status:
            self.tick()

    def tick(self):
        ret, frame = self.VideoInput.grab_frame()
        processed_frame, results = self.Processor.process_frame(frame)
        self.DataSink.push_data(results)
        self.VideoOutput.push_frame(processed_frame)

    def stop(self):
        self.status = False
        self.VideoInput.stop()
        self.DataSink.stop()
        self.VideoOutput.stop()
        self.Processor.stop()
