def flatten_dict(d, delimiter='.'):
    def expand(key, value):
        if key == 'customData':
            return [('{}[{}]'.format(key, k), v) for k, v in value.items()]
        elif isinstance(value, dict):
            return [
                (delimiter.join([key, k]), v)
                for k, v in flatten_dict(value, delimiter).items()
                ]
        else:
            return [(key, value)]

    return dict(
        [item for k, v in d.items() for item in expand(k, v)]
    )
