# pencepay-python
An implementation of the pencepay.com payment method


# Quick Start

## Step 1: Setup

```python
from pencepay.settings.config import Context

Context.set_public_key('your-public-key')
Context.set_secret_key('your-secret-key')
```

## Step 2: Create the `Request` objects

### Simple `Customer Request`
```python
from pencepay.request import CustomerRequest

customer_request =  CustomerRequest(firstName='John', lastName='Hancock', email='hancock@server.com')

OR

customer_request = CustomerRequest()
customer_request.firstName='John' 
customer_request.lastName='Hancock' 
customer_request.email='hancock@server.com'

```
For `AddressRequest`, `CreditCardRequest` and `SettingsRequest` things are pretty similar.

### A more complex `Transaction Request`

```python
from pencepay.request import CustomerRequest, CreditCardRequest, AddressRequest, TransactionRequest

customer_request = CustomerRequest(
    firstName='John',
    lastName='Hancock',
    email='hancock@server.com'
)
card_request = CreditCardRequest(
    cardholderName='John Hancock',
    number='4350100010001002',
    cvv='313',
    expiryMonth='12',
    expiryYear='2018'
)
address_request = AddressRequest(
    city='Zagreb',
    postalCode='10000',
    countryCode='HR'
)
transaction_request = TransactionRequest(
    orderId='1234',
    amount=55.5,
    currencyCode='USD',
    customer=customer_request,
    billingAddress=address_request,
    creditCard=card_request
)

```



## Step 3: Send data to Pancepay

### Send a single Customer
```python
from pencepay.services import Customer

response = Customer().create(request=customer_request)
```

### Perform a Transaction
```python
from pencepay.services import Transaction

response = Transaction().create(request=transaction_request)
```

For more information about how to use our api, please check the `tests` ([here](https://github.com/opencbsoft/pencepay-python/tree/master/pencepay/tests) are more examples).
