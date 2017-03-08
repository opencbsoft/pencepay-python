from pencepay.settings.choices import ActionChoices as actions
from pencepay.settings.choices import APIChoices as api

ENDPOINTS = {
    api.TRANSACTIONS: {
        actions.CREATE: {
            'method': 'POST',
            'path': '/transaction',
        },
        actions.SEARCH: {
            'method': 'GET',
            'path': '/transactions'
        },
        actions.FIND: {
            'method': 'GET',
            'path': '/transaction/{uid}'
        },
        actions.VOID: {
            'method': 'POST',
            'path': '/transaction/{uid}/void'
        },
        actions.CAPTURE: {
            'method': 'POST',
            'path': '/transaction/{uid}/capture'
        },
        actions.REFUND: {
            'method': 'POST',
            'path': '/transaction/{uid}/refund'
        }
    },
    api.CUSTOMERS: {
        actions.CREATE: {
            'method': 'POST',
            'path': '/customer',
        },
        actions.FIND: {
            'method': 'GET',
            'path': '/customer/{uid}'
        },
        actions.SEARCH: {
            'method': 'GET',
            'path': '/customers'
        },
        actions.UPDATE: {
            'method': 'POST',
            'path': '/customer/{uid}'
        },
        actions.DELETE: {
            'method': 'DELETE',
            'path': '/customer/{uid}'
        }
    },
    api.CARDS: {
        actions.CREATE: {
            'method': 'POST',
            'path': '/customer/{customer_uid}/card',
        },
        actions.SEARCH: {
            'method': 'GET',
            'path': '/customer/{customer_uid}/cards'
        },
        actions.FIND: {
            'method': 'GET',
            'path': '/customer/{customer_uid}/card/{uid}'
        },
        actions.UPDATE: {
            'method': 'POST',
            'path': '/customer/{customer_uid}/card/{uid}'
        },
        actions.DELETE: {
            'method': 'DELETE',
            'path': '/customer/{customer_uid}/card/{uid}'
        }
    },
    api.ADDRESSES: {
        actions.CREATE: {
            'method': 'POST',
            'path': '/customer/{customer_uid}/address',
        },
        actions.SEARCH: {
            'method': 'GET',
            'path': '/customer/{customer_uid}/addresses'
        },
        actions.FIND: {
            'method': 'GET',
            'path': '/customer/{customer_uid}/address/{uid}'
        },
        actions.UPDATE: {
            'method': 'POST',
            'path': '/customer/{customer_uid}/address/{uid}'
        },
        actions.DELETE: {
            'method': 'DELETE',
            'path': '/customer/{customer_uid}/address/{uid}'
        }
    },
    api.BANK_ACCOUNTS: {
        actions.CREATE: {
            'method': 'POST',
            'path': '/customer/{customer_uid}/bank_account',
        },
        actions.SEARCH: {
            'method': 'GET',
            'path': '/customer/{customer_uid}/bank_accounts'
        },
        actions.FIND: {
            'method': 'GET',
            'path': '/customer/{customer_uid}/bank_account/{uid}'
        },
        actions.UPDATE: {
            'method': 'POST',
            'path': '/customer/{customer_uid}/bank_account/{uid}'
        },
        actions.DELETE: {
            'method': 'DELETE',
            'path': '/customer/{customer_uid}/bank_account/{uid}'
        }
    },
    api.PAYCODES: {
        actions.CREATE: {
            'method': 'POST',
            'path': '/paycode',
        },
        actions.FIND: {
            'method': 'GET',
            'path': '/paycode/{uid}'
        },
        actions.SEARCH: {
            'method': 'GET',
            'path': '/paycodes'
        },
        actions.UPDATE: {
            'method': 'POST',
            'path': '/paycode/{uid}'
        },
        actions.DELETE: {
            'method': 'DELETE',
            'path': '/paycode/{uid}'
        }
    },
    api.TAGS: {
        actions.CREATE: {
            'method': 'POST',
            'path': '/tag',
        },
        actions.FIND: {
            'method': 'GET',
            'path': '/tag/{uid}'
        },
        actions.SEARCH: {
            'method': 'GET',
            'path': '/tags'
        },
        actions.UPDATE: {
            'method': 'POST',
            'path': '/tag/{uid}'
        },
        actions.DELETE: {
            'method': 'DELETE',
            'path': '/tag/{uid}'
        }
    },
    api.EVENTS: {
        actions.SEARCH: {
            'method': 'GET',
            'path': '/events/'
        },
        actions.FIND: {
            'method': 'GET',
            'path': '/event/{uid}'
        },
    }
}
