from marshmallow import Schema
from marshmallow.fields import Field

from pencepay.settings.choices import ActionChoices
from pencepay.settings.endpoints import ENDPOINTS
from pencepay.utils.functions import flatten_dict
from pencepay.utils.http_client import HttpClient
from pencepay.utils.serializer import Serializer


class RequestMetaclass(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)

        field_map = {k: v for k, v in cls.__dict__.items() if isinstance(v, Field)}
        cls.serializer_class = type('RequestSerializer', (Schema,), field_map.copy())

        for name, value in field_map.items():
            try:
                delattr(cls, name)
            except AttributeError:
                continue


class BaseRequest(metaclass=RequestMetaclass):
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def get_data(self):
        # self.validate() TODO: decide if we need validation.
        serializer = self.__class__.serializer_class()
        return serializer.dump(self).data

    def get_flattened_data(self):
        data = self.get_data()
        flattened_data = flatten_dict(data)
        return flattened_data

    @classmethod
    def as_field(cls, **kwargs):
        return cls.serializer_class

    def validate(self):
        """
        Implement this method to add custom validation.
        """
        pass


class BaseService(object):
    action = None
    api = None
    request = None
    endpoints = ENDPOINTS

    def _http_request(self, **kwargs):
        client = HttpClient()

        method = self.endpoints[self.api][self.action]['method']
        path = self.endpoints[self.api][self.action]['path'].format(**kwargs)
        params = {}

        if self.action in (ActionChoices.CREATE, ActionChoices.UPDATE, ActionChoices.CAPTURE, ActionChoices.REFUND):
            assert self.request is not None
            params = self.request.get_flattened_data()

        elif self.action == ActionChoices.SEARCH:
            assert 'params' in kwargs
            params = kwargs.get('params')

        response = client.request(method=method, path=path, params=params)
        return response


class CRUDBasedServiceMixin:
    action = None
    request = None

    def create(self, request):
        self.action = 'create'
        self.request = request
        response = self._http_request()
        return response

    def find(self, uid: str):
        self.action = 'find'
        return self._http_request(uid=uid)

    def search(self, params: dict):
        self.action = 'search'
        return self._http_request(params=params)

    def update(self, uid: str, request):
        self.action = 'update'
        self.request = request
        return self._http_request(uid=uid)

    def delete(self, uid: str):
        self.action = 'delete'
        return self._http_request(uid=uid)


class CustomerBasedServiceMixin:
    def __init__(self, customer_uid):
        self.customer_uid = customer_uid
        super().__init__()

    def _http_request(self, **kwargs):
        kwargs['customer_uid'] = self.customer_uid

        return super()._http_request(**kwargs)
