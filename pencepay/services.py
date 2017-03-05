import hashlib

from pencepay.request import EventRequest
from pencepay.settings.choices import APIChoices
from pencepay.settings.config import Context
from pencepay.utils.base import CustomerBasedServiceMixin, CRUDBasedServiceMixin, BaseService


class CreditCard(CustomerBasedServiceMixin, CRUDBasedServiceMixin, BaseService):
    api = APIChoices.CARDS


class Address(CustomerBasedServiceMixin, CRUDBasedServiceMixin, BaseService):
    api = APIChoices.ADDRESSES


class Customer(BaseService, CRUDBasedServiceMixin):
    api = APIChoices.CUSTOMERS


class Event(BaseService):
    api = APIChoices.EVENTS

    def find(self, uid: str):
        self.action = 'find'
        return self._http_request(uid=uid)

    def search(self, params: dict):
        self.action = 'search'
        return self._http_request(params=params)

    def parse(self, post_body, check_authenticity=False):
        event = EventRequest.get_object(post_body)

        if check_authenticity and event:
            result = self.find(event.uid)
            if result.status_code > 300:
                raise Exception("Authenticity failed for this event: uid: {uid}.")

        return event


class Transaction(BaseService):
    api = APIChoices.TRANSACTIONS
    action = None

    def create(self, request):
        self.action = 'create'
        self.request = request
        return self._http_request()

    def find(self, uid: str):
        self.action = 'find'
        return self._http_request(uid=uid)

    def search(self, params: dict):
        self.action = 'search'
        return self._http_request(params=params)

    def void(self, uid: str):
        self.action = 'void'
        return self._http_request(uid=uid)

    def capture(self, uid: str, request):
        self.action = 'capture'
        self.request = request
        return self._http_request(uid=uid)

    def refund(self, uid: str, request):
        self.action = 'refund'
        self.request = request
        return self._http_request(uid=uid)

    @staticmethod
    def generate_checkout_parameters(request):
        required = ('amount', 'currencyCode', 'orderId', 'cancelUrl', 'redirectUrl')
        params = request.get_flattened_data()

        for property_name in required:
            if property_name not in params:
                raise Exception('{name} is missing'.format(name=property_name))

        params['apiVersion'] = Context.api_version
        params['publicKey'] = Context.public_key

        signature_fields = ('publicKey', 'amount', 'currencyCode', 'orderId')

        digest_input = ''.join(str(params[field]) for field in signature_fields)
        digest_input += Context.secret_key

        hash_input = hashlib.sha256(digest_input.encode('utf-8')).hexdigest()

        params['signature'] = hash_input

        return params
