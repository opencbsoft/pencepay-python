from serpy import StrField, FloatField, IntField, BoolField

from pencepay.utils.base import BaseRequest
from pencepay.utils.exceptions import ValidationError


class AddressRequest(BaseRequest):
    city = StrField()
    postalCode = StrField()
    countryCode = StrField()


class CustomerRequest(BaseRequest):
    name = StrField(required=False)
    firstName = StrField(required=False)
    lastName = StrField(required=False)
    email = StrField()


class CreditCardRequest(BaseRequest):
    cardholderName = StrField()
    number = StrField()
    cvv = StrField()
    expiryMonth = IntField()
    expiryYear = IntField()


class SettingsRequest(BaseRequest):
    saveInSafe = BoolField(required=False)
    reserveFundsOnly = BoolField(required=False)
    locale = StrField(required=False)


class TransactionRequest(BaseRequest):
    paymentMethod = StrField(required=False)
    creditCardUid = StrField(required=False)
    orderId = StrField(required=False)
    description = StrField(required=False)
    amount = FloatField()
    currencyCode = StrField()
    requestIpAddress = StrField(required=False)
    cancelUrl = StrField(required=False)
    redirectUrl = StrField(required=False)
    customer = CustomerRequest.as_field(required=False)
    billingAddress = AddressRequest.as_field(required=False)
    creditCard = CreditCardRequest.as_field(required=False)
    settings = SettingsRequest.as_field(required=False)

    def validate(self):
        data = self.__dict__
        if not data.get('creditCardUid') and not data.get('creditCard'):
            raise ValidationError("'creditCardUid' or 'creditCard' is needed.")


class AmountTransactionRequest(BaseRequest):
    amount = FloatField()
