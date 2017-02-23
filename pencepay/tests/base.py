import os

from pencepay.settings.config import Context


class HTTPRequestTest:
    @classmethod
    def setup_class(cls):
        Context.set_public_key(os.environ.get('PENCEPAY_PUBLIC_KEY'))
        Context.set_secret_key(os.environ.get('PENCEPAY_SECRET_KEY'))
        cls.expected_parameters = {
            'auth': (Context.public_key, Context.secret_key),
            'headers': {
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            },
        }
