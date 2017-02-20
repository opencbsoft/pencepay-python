import serpy


class Serializer(serpy.Serializer):
    def _serialize(self, instance, fields):
        v = {}
        for name, getter, to_value, call, required, pass_self in fields:
            if pass_self:
                result = getter(self, instance)
            else:
                try:
                    result = getter(instance)
                except AttributeError as e:
                    if required:
                        raise e
                    else:
                        continue

                if required or result is not None:
                    if call:
                        result = result()
                    if to_value:
                        result = to_value(result)
            v[name] = result

        return v
