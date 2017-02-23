import requests

from pencepay.settings.config import Context
from pencepay.utils.exceptions import ValidationError
from pencepay.utils.logger import get_logger

logger = get_logger(__name__)


class HttpClient(object):
    def __init__(self):
        if not Context.public_key or not Context.secret_key:
            raise ValidationError("Public key or Secret key is missing. Please use 'Context' class to set them.")

        self.public_key = Context.public_key
        self.secret_key = Context.secret_key
        self.api_base_url = Context.api_base_url

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
        response = requests.request(method, url, **kwargs)

        if response.status_code > 200:
            logger.error(response.text)

        return response
