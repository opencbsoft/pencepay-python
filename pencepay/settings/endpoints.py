from pencepay.settings.choices import ActionChoices

ENDPOINTS = {
    'transactions': {
        ActionChoices.CREATE: {
            'method': 'POST',
            'path': '/transaction',
        },
        ActionChoices.SEARCH: {
            'method': 'GET',
            'path': '/transactions'
        },
        ActionChoices.FIND: {
            'method': 'GET',
            'path': '/transaction/{uid}'
        },
        ActionChoices.VOID: {
            'method': 'POST',
            'path': '/transaction/{uid}/void'
        },
        ActionChoices.CAPTURE: {
            'method': 'POST',
            'path': '/transaction/{uid}/capture'
        },
        ActionChoices.REFUND: {
            'method': 'POST',
            'path': '/transaction/{uid}/refund'
        }
    },
    'customers': {
        ActionChoices.CREATE: {
            'method': 'POST',
            'path': '/customer',
        },
        ActionChoices.FIND: {
            'method': 'GET',
            'path': '/customer/{uid}'
        },
        ActionChoices.SEARCH: {
            'method': 'GET',
            'path': '/customers'
        },
        ActionChoices.UPDATE: {
            'method': 'POST',
            'path': '/customer/{uid}'
        },
        ActionChoices.DELETE: {
            'method': 'DELETE',
            'path': '/customer/{uid}'
        }
    },
    'cards': {
        ActionChoices.CREATE: {
            'method': 'POST',
            'path': '/customer/{customer_uid}/card',
        },
        ActionChoices.SEARCH: {
            'method': 'GET',
            'path': '/customer/{customer_uid}/cards'
        },
        ActionChoices.FIND: {
            'method': 'GET',
            'path': '/customer/{customer_uid}/card/{uid}'
        },
        ActionChoices.UPDATE: {
            'method': 'POST',
            'path': '/customer/{customer_uid}/card/{uid}'
        },
        ActionChoices.DELETE: {
            'method': 'DELETE',
            'path': '/customer/{customer_uid}/card/{uid}'
        }
    },
    'addresses': {
        ActionChoices.CREATE: {
            'method': 'POST',
            'path': '/customer/{customer_uid}/address',
        },
        ActionChoices.SEARCH: {
            'method': 'GET',
            'path': '/customer/{customer_uid}/addresses'
        },
        ActionChoices.FIND: {
            'method': 'GET',
            'path': '/customer/{customer_uid}/address/{uid}'
        },
        ActionChoices.UPDATE: {
            'method': 'POST',
            'path': '/customer/{customer_uid}/address/{uid}'
        },
        ActionChoices.DELETE: {
            'method': 'DELETE',
            'path': '/customer/{customer_uid}/address/{uid}'
        }
    },
    'events': {
        ActionChoices.SEARCH: {
            'method': 'GET',
            'path': '/events/'
        },
        ActionChoices.FIND: {
            'method': 'GET',
            'path': '/event/{uid}'
        },
    }
}
