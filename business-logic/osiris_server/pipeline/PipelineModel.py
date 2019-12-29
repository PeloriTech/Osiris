from django.db import models
from django.contrib.auth.models import User


class Pipeline(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    input_stream = models.TextField()
    input_type = models.TextField()
    stream_processor = models.TextField()
    remote_address = models.TextField()
    videostream_port = models.IntegerField(default=-1)
    websocket_port = models.IntegerField(default=-1)
    pid = models.IntegerField(null=True)
