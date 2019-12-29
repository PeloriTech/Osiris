import requests
from osiris_server.settings import WOWZA_HOST


class WowzaGateway:

    @staticmethod
    def get_publishers() -> dict:
        server_url = WOWZA_HOST
        server_url += "/v3/servers/_defaultServer_/publishers"
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.get(server_url, headers=headers)
        return response.json()['predictions'][0]['classes']
