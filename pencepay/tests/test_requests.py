import pytest

from pencepay.request import AddressRequest, TransactionRequest, CustomerRequest, CreditCardRequest
from pencepay.utils.exceptions import ValidationError


class TestAddressRequest:
    def test_get_data(self):
        req = AddressRequest()
        req.city = 'Zagreb'
        req.postalCode = '10000'
        req.countryCode = 'HR'

        data = req.get_data()
        expected = {
            'city': 'Zagreb',
            'postalCode': '10000',
            'countryCode': 'HR'
        }

        assert data == expected


class TestCustomerRequest:
    def test_get_data(self):
        req = CustomerRequest()
        req.firstName = 'John'
        req.lastName = 'Hancock'
        req.email = 'hancock@server.com'

        data = req.get_data()
        expected = {
            'firstName': 'John',
            'lastName': 'Hancock',
            'email': 'hancock@server.com',
        }

        assert data == expected


class TestCreditCardRequest:
    def test_get_data(self):
        req = CreditCardRequest()
        req.cardholderName = 'John Hancock'
        req.number = '4350100010001002'
        req.cvv = '313'
        req.expiryMonth = '12'
        req.expiryYear = '2018'

        data = req.get_data()
        expected = {
            'cardholderName': 'John Hancock',
            'number': '4350100010001002',
            'cvv': '313',
            'expiryMonth': 12,
            'expiryYear': 2018,
        }

        assert data == expected


class TestTransactionRequest:
    @classmethod
    def setup_class(cls):
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
            postalCode='1000',
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

    def test_get_flattened_data(self):
        data = self.transaction_request.get_flattened_data()

        expected = {
            'orderId': '1234',
            'amount': 55.5,
            'currencyCode': 'USD',
            'customer.firstName': 'John',
            'customer.lastName': 'Hancock',
            'customer.email': 'hancock@server.com',
            'billingAddress.city': 'Zagreb',
            'billingAddress.postalCode': '1000',
            'billingAddress.countryCode': 'HR',
            'creditCard.cardholderName': 'John Hancock',
            'creditCard.number': '4350100010001002',
            'creditCard.cvv': '313',
            'creditCard.expiryMonth': 12,
            'creditCard.expiryYear': 2018,
        }

        assert data == expected

    def test_get_data(self):
        transaction_request = TransactionRequest()
        transaction_request.orderId = '1234'
        transaction_request.amount = 55.5
        transaction_request.currencyCode = 'USD'
        transaction_request.customer = self.customer_request
        transaction_request.billingAddress = self.address_request
        transaction_request.creditCard = self.card_request

        data = transaction_request.get_data()
        same_data = self.transaction_request.get_data()

        expected = {
            'orderId': '1234',
            'amount': 55.5,
            'currencyCode': 'USD',
            'customer': {
                'firstName': 'John',
                'lastName': 'Hancock',
                'email': 'hancock@server.com',
            },
            'billingAddress': {
                'city': 'Zagreb',
                'postalCode': '1000',
                'countryCode': 'HR'
            },
            'creditCard': {
                'cardholderName': 'John Hancock',
                'number': '4350100010001002',
                'cvv': '313',
                'expiryMonth': 12,
                'expiryYear': 2018,
            }
        }

        assert data == expected
        assert same_data == expected

    def test_using_card_uid(self):
        transaction_request = TransactionRequest()
        transaction_request.creditCardUid = 'some1234uid'
        transaction_request.amount = 55.5
        transaction_request.currencyCode = 'USD'

        data = transaction_request.get_data()
        expected = {
            'creditCardUid': 'some1234uid',
            'amount': 55.5,
            'currencyCode': 'USD'
        }

        assert data == expected

    @pytest.mark.skip
    def test_error_is_raised_when_card_and_carduid_is_missing(self):
        transaction_request = TransactionRequest()
        transaction_request.amount = 55.5
        transaction_request.currencyCode = 'USD'

        with pytest.raises(ValidationError):
            transaction_request.get_data()
