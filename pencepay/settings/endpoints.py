ENDPOINTS = {
    'transactions': {
        'create': {
            'method': 'POST',
            'path': '/transaction',
        },
        'search': {
            'method': 'GET',
            'path': '/transactions'
        },
        'find': {
            'method': 'GET',
            'path': '/transaction/{uid}'
        },
        'void': {
            'method': 'POST',
            'path': '/transaction/{uid}/void'
        },
        'capture': {
            'method': 'POST',
            'path': '/transaction/{uid}/capture'
        },
        'refund': {
            'method': 'POST',
            'path': '/transaction/{uid}/refund'
        }
    },
    'customers': {
        'create': {
            'method': 'POST',
            'path': '/customer',
        },
        'find': {
            'method': 'GET',
            'path': '/customer/{uid}'
        },
        'search': {
            'method': 'GET',
            'path': '/customers'
        },
        'update': {
            'method': 'POST',
            'path': '/customer/{uid}'
        },
        'delete': {
            'method': 'DELETE',
            'path': '/customer/{uid}'
        }
    },
    'cards': {
        'create': {
            'method': 'POST',
            'path': '/customer/{customer_uid}/card',
        },
        'search': {
            'method': 'GET',
            'path': '/customer/{customer_uid}/cards'
        },
        'find': {
            'method': 'GET',
            'path': '/customer/{customer_uid}/card/{uid}'
        },
        'update': {
            'method': 'POST',
            'path': '/customer/{customer_uid}/card/{uid}'
        },
        'delete': {
            'method': 'DELETE',
            'path': '/customer/{customer_uid}/card/{uid}'
        }
    },
    'addresses': {
        'create': {
            'method': 'POST',
            'path': '/customer/{customer_uid}/address',
        },
        'search': {
            'method': 'GET',
            'path': '/customer/{customer_uid}/addresses'
        },
        'find': {
            'method': 'GET',
            'path': '/customer/{customer_uid}/address/{uid}'
        },
        'update': {
            'method': 'POST',
            'path': '/customer/{customer_uid}/address/{uid}'
        },
        'delete': {
            'method': 'DELETE',
            'path': '/customer/{customer_uid}/address/{uid}'
        }
    },
    'events': {
        'search': {
            'method': 'GET',
            'path': '/events/'
        },
        'find': {
            'method': 'GET',
            'path': '/event/{uid}'
        },
    }
}
