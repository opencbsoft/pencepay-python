class ActionChoices:
    CREATE = 'create'
    FIND = 'find'
    SEARCH = 'search'
    VOID = 'void'
    CAPTURE = 'capture'
    REFUND = 'refund'
    UPDATE = 'update'
    DELETE = 'delete'


class APIChoices:
    TRANSACTIONS = 'transactions'
    ADDRESSES = 'addresses'
    CUSTOMERS = 'customers'
    CARDS = 'cards'
    BANK_ACCOUNTS = 'bank_accounts'
    PAYCODES = 'paycodes'
    EVENTS = 'events'


class CredentialsChoices:
    public_key = 'PENCEPAY_PUBLIC_KEY'
    secret_key = 'PENCEPAY_SECRET_KEY'
