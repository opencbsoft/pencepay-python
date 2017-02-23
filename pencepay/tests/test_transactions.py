from unittest.mock import Mock

import pytest

from pencepay.request import AmountTransactionRequest, SettingsRequest
from pencepay.request import CustomerRequest, CreditCardRequest, AddressRequest, TransactionRequest
from pencepay.services import Transaction
from pencepay.settings.config import Context
from pencepay.tests.base import HTTPRequestTest


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    request_mock = Mock()
    request_mock.return_value = Mock(status_code=200, text='some text')
    monkeypatch.setattr("requests.sessions.Session.request", request_mock)

    return request_mock


class TestTransactionService(HTTPRequestTest):
    @classmethod
    def setup_class(cls):
        super().setup_class()

        cls.customer_request = CustomerRequest(
            firstName='John',
            lastName='Hancock',
            email='hancock@server.com'
        )
        cls.card_request = CreditCardRequest(
            cardholderName='John Hancock',
            number='4350100010001002',
            cvv='313',
            expiryMonth='12',
            expiryYear='2018'
        )
        cls.address_request = AddressRequest(
            city='Zagreb',
            postalCode='10000',
            countryCode='HR'
        )
        cls.transaction_request = TransactionRequest(
            orderId='1234',
            amount=55.5,
            currencyCode='USD',
            customer=cls.customer_request,
            billingAddress=cls.address_request,
            creditCard=cls.card_request
        )

    def test_generate_checkout_parameters(self):
        req = TransactionRequest()

        req.orderId = '123456'
        req.description = 'Holiday in Croatia, June 2015'
        req.amount = 10.99
        req.currencyCode = 'EUR'
        req.cancelUrl = 'cancel-url-on-your-server'
        req.redirectUrl = 'redirect-url-on-your-server'
        req.billingAddress = self.address_request
        req.customer = self.customer_request
        req.settings = SettingsRequest(locale='hr-HR', reserveFundsOnly=True)

        Context.api_version = '1.0.4'
        Context.public_key = 'your-public-key'
        Context.secret_key = 'your-secret-key'

        data = Transaction.generate_checkout_parameters(request=req)
        expected = {
            'amount': 10.99,
            'currencyCode': 'EUR',
            'orderId': '123456',
            'description': 'Holiday in Croatia, June 2015',

            'customer.firstName': 'John',
            'customer.lastName': 'Hancock',
            'customer.email': 'hancock@server.com',
            'billingAddress.city': 'Zagreb',
            'billingAddress.postalCode': '10000',
            'billingAddress.countryCode': 'HR',
            'settings.reserveFundsOnly': True,
            'settings.locale': 'hr-HR',
            'cancelUrl': 'cancel-url-on-your-server',
            'redirectUrl': 'redirect-url-on-your-server',
            'apiVersion': '1.0.4',
            'publicKey': 'your-public-key',
            'signature': '4b13c88732ee001eae9dc30c69ea826949ac0c12afc6c51c2082163e57c277c5',
        }

        assert data == expected

    def test_create(self):
        response = Transaction().create(request=self.transaction_request)

        assert response.status_code == 200

    def test_create_with_card_uid(self):
        transaction_request = TransactionRequest()
        transaction_request.creditCardUid = 'card_X8I6pT7g7c7nxI'
        transaction_request.amount = 22
        transaction_request.currencyCode = 'EUR'

        response = Transaction().create(request=transaction_request)

        assert response.status_code == 200

    def test_find(self):
        response = Transaction().find(uid='txn_bfXLikzGG5igxn')

        assert response.status_code == 200

    def test_search(self):
        response = Transaction().search(params={'currencyCode': 'EUR'})

        assert response.status_code == 200

    def test_void(self):
        response = Transaction().void(uid='txn_ACenirxGG5ioxA')

        assert response.status_code == 200

    def test_capture(self):
        req = AmountTransactionRequest(amount=55)

        response = Transaction().capture(uid='txn_ACenirxGG5ioxA', request=req)

        assert response.status_code == 200

    def test_refund(self):
        req = AmountTransactionRequest(amount=55)

        response = Transaction().refund(uid='txn_ACenirxGG5ioxA', request=req)

        assert response.status_code == 200
