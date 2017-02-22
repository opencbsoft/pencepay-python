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

```python
from pencepay.request import CustomerRequest

request =  CustomerRequest(firstName='John', lastName='Hancock', email='hancock@server.com')

OR

request = CustomerRequest()
request.firstName='John' 
request.lastName='Hancock' 
request.email='hancock@server.com'

```


## Step 3: Send data to Pancepay

```python
from pencepay.services import Customer

response = Customer().create(request=request)
```

For more information about how to use our api, please check the `tests` ([here](https://github.com/opencbsoft/pencepay-python/tree/master/pencepay/tests) are more examples).
