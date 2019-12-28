
from django.urls import path

from osiris_server.user.UserViews import UserViews

urlpatterns = [
    path('register/', UserViews.register_user, name='register user'),
    path('login/', UserViews.login, name='_login'),
    path('get/', UserViews.get, name='get current user'),
    path('update/', UserViews.update, name='update user'),
    path('info/', UserViews.info, name='user info'),
    path('logged_in/', UserViews.is_logged_in, name='is logged in'),
]