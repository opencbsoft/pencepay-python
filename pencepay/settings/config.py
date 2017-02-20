class Singleton(type):
    instance = None

    def __call__(cls, *args, **kw):
        if not cls.instance:
            cls.instance = super().__call__(*args, **kw)

        return cls.instance

    def __setattr__(self, name, value):
        if hasattr(self, name):
            super().__setattr__(name, value)
        else:
            raise TypeError('Cannot set attributes directly on Context class.')


class Context(metaclass=Singleton):
    api_base_url = 'https://api.pencepay.com/v1'
    api_version = '1.0.4'
    public_key = None
    secret_key = None

    @classmethod
    def set_api_version(cls, api_version):
        cls.api_version = api_version

    @classmethod
    def set_public_key(cls, public_key):
        cls.public_key = public_key

    @classmethod
    def set_secret_key(cls, secret_key):
        cls.secret_key = secret_key

    def __setattr__(self, name, value):
        raise TypeError('Cannot set attributes directly on the Context class.')
