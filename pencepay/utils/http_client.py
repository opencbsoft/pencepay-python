import json

import requests

from pencepay.utils.logger import get_logger

logger = get_logger(__name__)


class HttpClient(object):
    api_base_url = 'https://api.pencepay.com/v1'

    def __init__(self, public_key, secret_key):
        self.public_key = public_key
        self.secret_key = secret_key

    def request(self, method: str, path: str, params: dict = None) -> object:
        kwargs = {
            'headers': {
                'Accept': "application/json",
                'Content-Type': "application/x-www-form-urlencoded;charset=UTF-8"
            },
            'auth': (self.public_key, self.secret_key)
        }

        if method.upper() == 'GET':
            kwargs['params'] = params
        else:
            kwargs['data'] = params

        url = self.api_base_url + path
        r = requests.request(method, url, **kwargs)

        if r.status_code > 200:
            logger.error(r.text)

        response = {
            'status_code': r.status_code,
            'body': json.loads(r.text)
        }

        return response
