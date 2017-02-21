import os

import pytest

from pencepay.request import CustomerRequest, CreditCardRequest, AddressRequest
from pencepay.services import CreditCard, Customer, Address
from pencepay.settings.choices import CredentialsChoices
from pencepay.settings.config import Context


class TestCustomerService:
    @classmethod
    def setup_class(cls):
        Context.set_public_key(os.environ.get(CredentialsChoices.public_key))
        Context.set_secret_key(os.environ.get(CredentialsChoices.secret_key))

        cls.customer_request = CustomerRequest(
            first_name='John',
            last_name='Hancock',
            email='hancock@server.com'
        )

        cls.customer_uid = 'cust_nLCjAco94iXGLC'

    @pytest.mark.skip
    def test_create(self):
        response = Customer().create(request=self.customer_request)

        assert response['status_code'] == 200

    def test_find(self):
        response = Customer().find(uid=self.customer_uid)

        assert response['status_code'] == 200

    def test_search(self):
        response = Customer().search({'email': 'hancock@server.com'})

        assert response['status_code'] == 200

    @pytest.mark.skip
    def test_update(self):
        response = Customer().update(uid=self.customer_uid, request=self.customer_request)

        assert response['status_code'] == 200

    @pytest.mark.skip
    def test_delete(self):
        response = Customer().delete(uid=self.customer_uid)

        assert response['status_code'] == 200


class TestCreditCardService:
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

    @pytest.mark.skip
    def test_create(self):
        response = CreditCard(customer_uid=self.customer_uid).create(request=self.card_request)

        assert response['status_code'] == 200

    # @pytest.mark.skip
    def test_find(self):
        response = CreditCard(customer_uid=self.customer_uid).find(uid='card_X8I6pT7g7c7nxI')

        assert response['status_code'] == 200

    # @pytest.mark.skip
    def test_search(self):
        response = CreditCard(customer_uid=self.customer_uid).search({'cvv': '313'})

        assert response['status_code'] == 200

    @pytest.mark.skip
    def test_update(self):
        response = CreditCard(customer_uid=self.customer_uid).update(uid='123', request=self.card_request)

        assert response['status_code'] == 200

    @pytest.mark.skip
    def test_delete(self):
        response = CreditCard(customer_uid=self.customer_uid).delete(uid='cust_rLu7LTgKbceGdu')

        assert response['status_code'] == 200


class TestAddressService:
    @classmethod
    def setup_class(cls):
        cls.address_request = AddressRequest(
            city='Zagreb',
            postal_code='1000',
            country_code='HR'
        )

        cls.customer_uid = 'cust_nLCjAco94iXGLC'

    @pytest.mark.skip
    def test_create(self):
        response = Address(customer_uid=self.customer_uid).create(request=self.address_request)

        assert response['status_code'] == 200

    # @pytest.mark.skip
    def test_find(self):
        response = Address(customer_uid=self.customer_uid).find(uid='addr_e5uEriGzATKpLu')

        assert response['status_code'] == 200

    # @pytest.mark.skip
    def test_search(self):
        response = Address(customer_uid=self.customer_uid).search({'city': 'Zagreb'})

        assert response['status_code'] == 200

    @pytest.mark.skip
    def test_update(self):
        request = AddressRequest(
            city='Zagreb',
            postal_code='1000',
            country_code='HR'
        )

        response = Address(customer_uid=self.customer_uid).update(uid='cust_rLu7LTgKbceGdu', request=request)

        assert response['status_code'] == 200

    @pytest.mark.skip
    def test_delete(self):
        response = Address(customer_uid=self.customer_uid).delete(uid='cust_rLu7LTgKbceGdu')

        assert response['status_code'] == 200
