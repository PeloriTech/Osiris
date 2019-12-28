import json

from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from osiris_server.user.TestUserData import TestUserData


class UserTest(TestCase):

    def test_register(self):
        response = self.client.post(reverse('register user'), json.dumps(TestUserData.register_info_2),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        user = User.objects.filter(username=TestUserData.register_info_2["username"])

        self.assertTrue(user)

    def test_login(self):
        self.client.post(reverse('register user'), json.dumps(TestUserData.register_info),
                                    content_type='application/json')
        response = self.client.post(reverse('_login'), json.dumps(TestUserData.login),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        self.client.post(reverse('register user'), json.dumps(TestUserData.register_info),
                         content_type='application/json')
        self.client.post(reverse('_login'), json.dumps(TestUserData.login),
                                    content_type='application/json')
        response = self.client.get(reverse('get current user'))
        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content)
        self.assertEqual(content['username'], TestUserData.register_info['username'])

    def test_update(self):
        self.client.post(reverse('register user'), json.dumps(TestUserData.register_info),
                         content_type='application/json')
        self.client.post(reverse('_login'), json.dumps(TestUserData.login),
                         content_type='application/json')
        response = self.client.post(reverse('update user'), json.dumps(TestUserData.update_info),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        user = User.objects.filter(username=TestUserData.register_info["username"]).first()

        self.assertEqual(user.username, TestUserData.update_info['username'])
        self.assertEqual(user.first_name, TestUserData.update_info['first_name'])
        self.assertEqual(user.last_name, TestUserData.update_info['last_name'])
        self.assertEqual(user.email, TestUserData.update_info['email'])
        self.assertTrue(authenticate(username=TestUserData.update_info['username'],
                                     password=TestUserData.update_info['password']
                                     ))

    def test_info(self):
        self.client.post(reverse('register user'), json.dumps(TestUserData.register_info),
                         content_type='application/json')
        self.client.post(reverse('register user'), json.dumps(TestUserData.register_info_2),
                         content_type='application/json')
        self.client.post(reverse('_login'), json.dumps(TestUserData.login),
                         content_type='application/json')
        response = self.client.post(reverse('user info'), json.dumps(TestUserData.info),
                         content_type='application/json')
        self.assertEqual(response.status_code, 200)

        user = User.objects.filter(username=TestUserData.register_info_2["username"]).first()
        content = json.loads(response.content)
        self.assertEqual(user.username, content['username'])
        self.assertEqual(user.first_name, content['first_name'])
        self.assertEqual(user.last_name, content['last_name'])
        self.assertEqual(user.email, content['email'])

    def test_is_logged_in(self):
        self.client.post(reverse('register user'), json.dumps(TestUserData.register_info),
                         content_type='application/json')
        self.client.post(reverse('_login'), json.dumps(TestUserData.login),
                         content_type='application/json')
        response = self.client.get(reverse('is logged in'))
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertTrue(content)
