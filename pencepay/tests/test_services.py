import json
from unittest.mock import Mock, patch

import pytest

from pencepay.request import CustomerRequest, CreditCardRequest, AddressRequest
from pencepay.services import CreditCard, Customer, Address, Event
from pencepay.tests.base import HTTPRequestTest


@pytest.fixture(autouse=True)
def requests_mock(monkeypatch):
    response_mock = Mock()
    response_mock.return_value = Mock(status_code=200, text='some text')
    monkeypatch.setattr("requests.sessions.Session.request", response_mock)

    return response_mock


class TestCustomerService(HTTPRequestTest):
    @classmethod
    def setup_class(cls):
        super().setup_class()

        cls.customer_request = CustomerRequest(
            firstName='John',
            lastName='Hancock',
            email='hancock@server.com'
        )

        cls.customer_uid = 'cust_nLCjAco94iXGLC'

    def test_create(self, requests_mock):
        response = Customer().create(request=self.customer_request)

        args = requests_mock.call_args[1]

        assert args['data']['email'] == 'hancock@server.com'

        assert response.status_code == 200

    def test_find(self, requests_mock):
        response = Customer().find(uid=self.customer_uid)

        args = requests_mock.call_args[1]

        assert self.customer_uid in args['url']
        assert args['method'] == 'GET'

        assert response.status_code == 200

    def test_search(self, requests_mock):
        response = Customer().search({'email': 'hancock@server.com'})

        args = requests_mock.call_args[1]

        assert 'email' in args['params']

        assert response.status_code == 200

    def test_update(self, requests_mock):
        response = Customer().update(uid=self.customer_uid, request=self.customer_request)

        args = requests_mock.call_args[1]

        assert self.customer_uid in args['url']
        assert args['method'] == 'POST'
        assert args['data']['lastName'] == 'Hancock'

        assert response.status_code == 200

    def test_delete(self, requests_mock):
        response = Customer().delete(uid=self.customer_uid)

        args = requests_mock.call_args[1]

        assert self.customer_uid in args['url']
        assert args['method'] == 'DELETE'

        assert response.status_code == 200


class TestCreditCardService(HTTPRequestTest):
    @classmethod
    def setup_class(cls):
        cls.card_request = CreditCardRequest(
            cardholderName='John Hancock',
            number='4350100010001002',
            cvv='313',
            expiryMonth='12',
            expiryYear='2018'
        )

        cls.customer_uid = 'cust_nLCjAco94iXGLC'

    def test_create(self, requests_mock):
        response = CreditCard(customer_uid=self.customer_uid).create(request=self.card_request)

        args = requests_mock.call_args[1]

        assert args['data']['number'] == '4350100010001002'
        assert args['method'] == 'POST'

        assert response.status_code == 200

    def test_find(self, requests_mock):
        response = CreditCard(customer_uid=self.customer_uid).find(uid='card_X8I6pT7g7c7nxI')

        args = requests_mock.call_args[1]

        assert self.customer_uid in args['url']
        assert 'card_X8I6pT7g7c7nxI' in args['url']
        assert args['method'] == 'GET'

        assert response.status_code == 200

    def test_search(self, requests_mock):
        response = CreditCard(customer_uid=self.customer_uid).search({'cvv': '313'})

        args = requests_mock.call_args[1]

        assert self.customer_uid in args['url']
        assert args['params']['cvv'] == '313'
        assert args['method'] == 'GET'

        assert response.status_code == 200

    def test_update(self, requests_mock):
        response = CreditCard(customer_uid=self.customer_uid).update(uid='123', request=self.card_request)

        args = requests_mock.call_args[1]

        assert self.customer_uid in args['url']
        assert '123' in args['url']
        assert args['data']['cvv'] == '313'
        assert args['method'] == 'POST'

        assert response.status_code == 200

    def test_delete(self, requests_mock):
        response = CreditCard(customer_uid=self.customer_uid).delete(uid='cust_rLu7LTgKbceGdu')

        args = requests_mock.call_args[1]

        assert self.customer_uid in args['url']
        assert args['method'] == 'DELETE'

        assert response.status_code == 200


class TestAddressService(HTTPRequestTest):
    @classmethod
    def setup_class(cls):
        cls.address_request = AddressRequest(
            city='Zagreb',
            postalCode='1000',
            countryCode='HR'
        )

        cls.customer_uid = 'cust_nLCjAco94iXGLC'

    def test_create(self, requests_mock):
        response = Address(customer_uid=self.customer_uid).create(request=self.address_request)

        args = requests_mock.call_args[1]

        assert self.customer_uid in args['url']
        assert args['data']['city'] == 'Zagreb'
        assert args['method'] == 'POST'
        assert response.status_code == 200

    def test_find(self, requests_mock):
        response = Address(customer_uid=self.customer_uid).find(uid='addr_e5uEriGzATKpLu')

        args = requests_mock.call_args[1]

        assert self.customer_uid in args['url']
        assert 'addr_e5uEriGzATKpLu' in args['url']
        assert args['method'] == 'GET'
        assert response.status_code == 200

    def test_search(self, requests_mock):
        response = Address(customer_uid=self.customer_uid).search({'city': 'Zagreb'})

        args = requests_mock.call_args[1]

        assert self.customer_uid in args['url']
        assert args['params']['city'] == 'Zagreb'
        assert args['method'] == 'GET'
        assert response.status_code == 200

    def test_update(self, requests_mock):
        request = AddressRequest(
            city='Zagreb',
            postalCode='1000',
            countryCode='HR'
        )

        response = Address(customer_uid=self.customer_uid).update(uid='cust_rLu7LTgKbceGdu', request=request)

        args = requests_mock.call_args[1]

        assert self.customer_uid in args['url']
        assert 'cust_rLu7LTgKbceGdu' in args['url']
        assert args['data']['countryCode'] == 'HR'
        assert args['method'] == 'POST'

        assert response.status_code == 200

    def test_delete(self, requests_mock):
        response = Address(customer_uid=self.customer_uid).delete(uid='cust_rLu7LTgKbceGdu')

        args = requests_mock.call_args[1]

        assert self.customer_uid in args['url']
        assert 'cust_rLu7LTgKbceGdu' in args['url']
        assert args['method'] == 'DELETE'
        assert response.status_code == 200


class TestEventService(HTTPRequestTest):
    def test_find(self, requests_mock):
        response = Event().find(uid='evnt_rt7oiejK56iKME')

        args = requests_mock.call_args[1]

        assert 'evnt_rt7oiejK56iKME' in args['url']
        assert args['method'] == 'GET'
        assert response.status_code == 200

    def test_search(self, requests_mock):
        response = Event().search({'objectUid': 'evnt_rt7oiejK56iKME'})

        args = requests_mock.call_args[1]

        assert args['params']['objectUid'] == 'evnt_rt7oiejK56iKME'
        assert args['method'] == 'GET'
        assert response.status_code == 200

    def test_parse(self):
        with open('pencepay/tests/data/event.json') as f:
            data = json.load(f)

        event = Event().parse(data)

        assert event.uid == data['uid']
        assert event.transaction.paymentMethod == data['transaction']['paymentMethod']
        assert event.transaction.creditCard.cardholderName == data['transaction']['creditCard']['cardholderName']

    def test_parse_authenticity(self, requests_mock):
        with open('pencepay/tests/data/event.json') as f:
            data = json.load(f)

        event = Event().parse(data, check_authenticity=True)

        assert event.uid == data['uid']
        assert event.transaction.paymentMethod == data['transaction']['paymentMethod']
        assert event.transaction.creditCard.cardholderName == data['transaction']['creditCard']['cardholderName']

        args = requests_mock.call_args[1]

        assert 'evnt_rt7oiejK56iKME' in args['url']
        assert args['method'] == 'GET'

    @patch('requests.sessions.Session.request')
    def test_parse_authenticity_raises_error(self, requests_mock):
        requests_mock.return_value = Mock(status_code=404, text='some text')

        with open('pencepay/tests/data/event.json') as f:
            data = json.load(f)

        with pytest.raises(Exception):
            event = Event().parse(data, check_authenticity=True)
