from serpy import Field

from pencepay.utils.functions import flatten_dict
from pencepay.utils.serializer import Serializer


class RequestMetaclass(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)

        field_map = {k: v for k, v in cls.__dict__.items() if isinstance(v, Field)}
        cls.serializer_class = type('RequestSerializer', (Serializer,), field_map.copy())

        for name, value in field_map.items():
            try:
                delattr(cls, name)
            except AttributeError:
                continue


class BaseRequest(metaclass=RequestMetaclass):
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def get_data(self):
        # self.validate() TODO: decide if we need validation.
        return self.__class__.serializer_class(self).data

    def get_flattened_data(self):
        data = self.get_data()
        flattened_data = flatten_dict(data)
        return flattened_data

    @classmethod
    def as_field(cls, **kwargs):
        return cls.serializer_class(**kwargs)

    def validate(self):
        """
        Implement this method to add custom validation.
        """
        pass
