
from django.urls import path

from osiris_server.pipeline.PipelineViews import PipelineViews

urlpatterns = [
    path('launch/', PipelineViews.launch, name='pipeline launch'),
    path('get/publishers/', PipelineViews.get_publishers, name='pipeline get publishers'),
    path('start/', PipelineViews.start, name='pipeline start'),
    path('list/', PipelineViews.list, name='pipeline list'),
    path('stop/', PipelineViews.stop, name='pipeline stop'),
    path('terminate/', PipelineViews.terminate, name='pipeline terminate')
]
