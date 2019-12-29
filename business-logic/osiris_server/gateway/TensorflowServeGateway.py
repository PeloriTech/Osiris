import requests

from osiris_server.settings import TENSORFLOW_SERVE_URL


class TensorflowServeGateway:

    url_predict= '/v1/models/{}:predict'

    @staticmethod
    def predict(jpeg_bytes, model) -> int:
        server_url = TENSORFLOW_SERVE_URL
        server_url += TensorflowServeGateway.url_predict.format(model)
        predict_request = '{"instances" : [{"b64": "%s"}]}' % jpeg_bytes
        response = requests.post(server_url, data=predict_request)

        return response.json()['predictions'][0]['classes']