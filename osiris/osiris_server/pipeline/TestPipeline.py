import json
import os

from django.test import TestCase
from django.urls import reverse

from osiris_server.user.TestUserData import TestUserData
from osiris_server.pipeline.TestPipelineData import TestPipelineData

from osiris_server.pipeline.PipelineModel import Pipeline


class TestPipeline(TestCase):

    def test_launch(self):
        self.client.post(reverse('register user'), json.dumps(TestUserData.register_info),
                         content_type='application/json')
        response = self.client.post(reverse('_login'), json.dumps(TestUserData.login),
                         content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('pipeline launch'), json.dumps(TestPipelineData.launch),
                         content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        pid = content['pid']
        _id = content['id']
        self.assertEqual(content['owner']['username'], TestUserData.register_info['username'])
        self.assertEqual(content['input_stream'], TestPipelineData.launch_response['input_stream'])
        self.assertEqual(content['stream_processor'], TestPipelineData.launch_response['stream_processor'])
        pipeline = Pipeline.objects.filter(input_stream=TestPipelineData.launch_response['input_stream']).first()
        self.assertIsNotNone(pipeline)

        self.assertEqual(pipeline.stream_processor, TestPipelineData.launch_response['stream_processor'])
        self.client.post(reverse('pipeline terminate'), json.dumps(_id),
                                    content_type='application/json')
        os.system('kill {}'.format(pid))

    def test_list(self):
        self.client.post(reverse('register user'), json.dumps(TestUserData.register_info),
                         content_type='application/json')
        response = self.client.post(reverse('_login'), json.dumps(TestUserData.login),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('pipeline launch'), json.dumps(TestPipelineData.launch),
                                    content_type='application/json')
        content = json.loads(response.content)
        pid = content['pid']
        _id = content['id']
        response = self.client.get(reverse('pipeline list'))
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        first_pipeline = content[0]
        self.assertEqual(first_pipeline['owner']['username'], TestUserData.register_info['username'])
        self.assertEqual(first_pipeline['input_stream'], TestPipelineData.launch_response['input_stream'])
        self.assertEqual(first_pipeline['remote_address'], TestPipelineData.launch_response['remote_address'])
        self.assertEqual(first_pipeline['stream_processor'], TestPipelineData.launch_response['stream_processor'])

        self.client.post(reverse('pipeline terminate'), json.dumps(_id),
                         content_type='application/json')
        os.system('kill {}'.format(pid))

    def test_stop(self):
        self.client.post(reverse('register user'), json.dumps(TestUserData.register_info),
                         content_type='application/json')
        response = self.client.post(reverse('_login'), json.dumps(TestUserData.login),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('pipeline launch'), json.dumps(TestPipelineData.launch),
                         content_type='application/json')
        content = json.loads(response.content)
        _id = content['id']
        pid = content['pid']
        response = self.client.post(reverse('pipeline stop'), json.dumps({'id':_id}),
                         content_type='application/json')
        pipeline = Pipeline.objects.filter(id=json.dumps(_id)).first()
        self.assertIsNotNone(pipeline)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('pipeline terminate'), json.dumps({'id':_id}),
                                    content_type='application/json')
        os.system('kill {}'.format(pid))

    def test_terminate(self):
        self.client.post(reverse('register user'), json.dumps(TestUserData.register_info),
                         content_type='application/json')
        response = self.client.post(reverse('_login'), json.dumps(TestUserData.login),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('pipeline launch'), json.dumps(TestPipelineData.launch),
                                    content_type='application/json')
        content = json.loads(response.content)
        _id = content['id']
        pid = content['pid']
        response = self.client.post(reverse('pipeline terminate'), json.dumps({'id':_id}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        pipeline = Pipeline.objects.filter(id=content['id']).first()
        self.assertIsNone(pipeline)
        os.system('kill {}'.format(pid))
