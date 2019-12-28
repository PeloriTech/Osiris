
from osiris.VideoOutput.VideoOutputTemplate import VideoOutputTemplate
from osiris.Processor.ProcessorTemplate import ProcessorTemplate
from osiris.VideoSource.VideoSourceTemplate import VideoSourceTemplate


class SimplePipelineTemplate:

    def __init__(self, videoInputTemplate:VideoSourceTemplate, videoOutputTemplate:VideoOutputTemplate, processorTemplate:ProcessorTemplate, dataSinkTemplate):

        self.video_input_template = videoInputTemplate
        self.video_output_template = videoOutputTemplate
        self.processor_template = processorTemplate
        self.data_sink_template = dataSinkTemplate


    def to_json(self):
        pass

    @staticmethod
    def parse_from_json(json_obj:dict):
        pass