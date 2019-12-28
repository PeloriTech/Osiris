
from osiris.VideoSource import VideoSourceFactory
from osiris.Processor import ProcessorFactory
from osiris.VideoOutput import VideoOutputFactory
from .SimplePipelineTemplate import SimplePipelineTemplate
from .SimplePipelineFactory import SimplePipelineFactory

class SimplePipelineController: # Should this be at django but not here?

    @staticmethod
    def create_pipeline(template:SimplePipelineTemplate):
        spf = SimplePipelineFactory()

        return spf.create_pipeline(template)







