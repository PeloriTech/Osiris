

from .SimplePipelineTemplate import SimplePipelineTemplate
from osiris.Processor.ProcessorFactory import ProcessorFactory
from osiris.VideoSource.VideoSourceFactory import VideoSourceFactory
from osiris.VideoOutput import VideoOutputFactory
from osiris.DataSink.DataSinkFactory import DataSinkFactory
from .SimplePipeline import SimplePipeline

class SimplePipelineFactory:

    @staticmethod
    def create_pipeline(pipelineTemplate:SimplePipelineTemplate):

        pFactory = ProcessorFactory() #factories can be static since they will be hard coded?
        processor = pFactory.create_processor(pipelineTemplate.processor_template)

        vfactory = VideoSourceFactory()
        videoSource = vfactory.create_input_source(pipelineTemplate.video_input_template)

        voFactory = VideoOutputFactory()
        videoOutput = voFactory.create_video_output(pipelineTemplate.video_output_template)

        dataSinkFactory = DataSinkFactory()
        dataSink = dataSinkFactory.create_data_sink(pipelineTemplate.data_sink_template)

        return SimplePipeline(videoSource, processor, dataSink, videoOutput)






