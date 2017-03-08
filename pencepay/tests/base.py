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


class CrudTestMixin:
    service_class = None
    request = None
    customer = {}

    def test_create(self, requests_mock):
        response = self.service_class(**self.customer).create(request=self.request)

        args = requests_mock.call_args[1]

        if 'customer_id' in self.customer:
            assert self.customer['customer_id'] in args['url']

        assert args['data']['iban'] == 'GB0000000000000'
        assert args['method'] == 'POST'
        assert response.status_code == 200

    def test_find(self, requests_mock):
        response = self.service_class(**self.customer).find(uid='ba_nLCjATog6cXGLC')

        args = requests_mock.call_args[1]

        if 'customer_id' in self.customer:
            assert self.customer['customer_id'] in args['url']

        assert 'ba_nLCjATog6cXGLC' in args['url']
        assert args['method'] == 'GET'
        assert response.status_code == 200

    def test_search(self, requests_mock):
        response = self.service_class(**self.customer).search({'bic': 'GB001BIC'})

        args = requests_mock.call_args[1]

        if 'customer_id' in self.customer:
            assert self.customer['customer_id'] in args['url']

        assert args['params']['bic'] == 'GB001BIC'
        assert args['method'] == 'GET'
        assert response.status_code == 200

    def test_update(self, requests_mock):
        request = self.service_class()
        request.accountHolder = 'John Hancock'
        request.accountNumber = '1111112222'
        request.iban = 'ES0000000000000'
        request.bic = 'GB001BIC'
        request.countryCode = 'ES'

        response = self.service_class(**self.customer).update(uid='ba_nLCjATog6cXGLC', request=request)

        args = requests_mock.call_args[1]

        if 'customer_id' in self.customer:
            assert self.customer['customer_id'] in args['url']

        assert 'ba_nLCjATog6cXGLC' in args['url']
        assert args['data']['countryCode'] == 'ES'
        assert args['method'] == 'POST'

        assert response.status_code == 200

    def test_delete(self, requests_mock):
        response = self.service_class(**self.customer).delete(uid='ba_nLCjATog6cXGLC')

        args = requests_mock.call_args[1]

        if 'customer_id' in self.customer:
            assert self.customer['customer_id'] in args['url']

        assert 'ba_nLCjATog6cXGLC' in args['url']
        assert args['method'] == 'DELETE'
        assert response.status_code == 200
