from marshmallow import fields

from pencepay.utils.base import BaseRequest
from pencepay.utils.exceptions import ValidationError


class AddressRequest(BaseRequest):
    city = fields.Str(required=True)
    postalCode = fields.Str(required=True)
    countryCode = fields.Str(required=True)


class CustomerRequest(BaseRequest):
    name = fields.Str(required=False)
    firstName = fields.Str(required=False)
    lastName = fields.Str(required=False)
    email = fields.Str(required=True)


class CreditCardRequest(BaseRequest):
    cardholderName = fields.Str(required=True)
    number = fields.Str(required=True)
    cvv = fields.Str(required=True)
    expiryMonth = fields.Int(required=True)
    expiryYear = fields.Int(required=True)


class SettingsRequest(BaseRequest):
    saveInSafe = fields.Bool(required=False)
    reserveFundsOnly = fields.Bool(required=False)
    locale = fields.Str(required=False)


class TransactionRequest(BaseRequest):
    paymentMethod = fields.Str(required=False)
    creditCardUid = fields.Str(required=False)
    orderId = fields.Str(required=False)
    description = fields.Str(required=False)
    amount = fields.Float(required=True)
    currencyCode = fields.Str(required=True)
    requestIpAddress = fields.Str(required=False)
    cancelUrl = fields.Str(required=False)
    redirectUrl = fields.Str(required=False)
    customer = fields.Nested(CustomerRequest.as_field(), required=False)
    billingAddress = fields.Nested(AddressRequest.as_field(), required=False)
    creditCard = fields.Nested(CreditCardRequest.as_field(), required=False)
    settings = fields.Nested(SettingsRequest.as_field(), required=False)

    def validate(self):
        data = self.__dict__
        if not data.get('creditCardUid') and not data.get('creditCard'):
            raise ValidationError("'creditCardUid' or 'creditCard' is needed.")


class AmountTransactionRequest(BaseRequest):
    amount = fields.Float(required=True)
