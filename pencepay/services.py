import hashlib
import json

from pencepay.request import EventRequest
from pencepay.settings.choices import APIChoices, ActionChoices
from pencepay.settings.config import Context
from pencepay.utils.base import CustomerBasedServiceMixin, CRUDBasedServiceMixin, BaseService


class CreditCard(CustomerBasedServiceMixin, CRUDBasedServiceMixin, BaseService):
    api = APIChoices.CARDS


class BankAccount(CustomerBasedServiceMixin, BaseService, CRUDBasedServiceMixin):
    api = APIChoices.BANK_ACCOUNTS


class Address(CustomerBasedServiceMixin, CRUDBasedServiceMixin, BaseService):
    api = APIChoices.ADDRESSES


class Customer(BaseService, CRUDBasedServiceMixin):
    api = APIChoices.CUSTOMERS


class PayCode(BaseService, CRUDBasedServiceMixin):
    api = APIChoices.PAYCODES


class Tag(BaseService, CRUDBasedServiceMixin):
    api = APIChoices.TAGS


class Event(BaseService):
    api = APIChoices.EVENTS

    def find(self, uid: str):
        self.action = ActionChoices.FIND
        return self._http_request(uid=uid)

    def search(self, params: dict):
        self.action = ActionChoices.SEARCH
        return self._http_request(params=params)

    def parse(self, post_body, check_authenticity=False):
        if isinstance(post_body, str):
            data = json.loads(post_body)
        elif isinstance(post_body, dict):
            data = post_body
        else:
            raise Exception("Unknown format. 'post_body' should be str or dict")

        event = EventRequest.get_object(data)

        if check_authenticity and event:
            result = self.find(event.uid)
            if result.status_code > 300:
                raise Exception("Authenticity failed for this event: uid: {uid}.")

        return event


class Transaction(BaseService):
    api = APIChoices.TRANSACTIONS
    action = None

    def create(self, request):
        self.action = ActionChoices.CREATE
        self.request = request
        return self._http_request()

    def find(self, uid: str):
        self.action = ActionChoices.FIND
        return self._http_request(uid=uid)

    def search(self, params: dict):
        self.action = ActionChoices.SEARCH
        return self._http_request(params=params)

    def void(self, uid: str):
        self.action = ActionChoices.VOID
        return self._http_request(uid=uid)

    def capture(self, uid: str, request):
        self.action = ActionChoices.CAPTURE
        self.request = request
        return self._http_request(uid=uid)

    def refund(self, uid: str, request):
        self.action = ActionChoices.REFUND
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
