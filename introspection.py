def introspection_info(obj):
    introspection_dict = \
        {'type': type(obj).__name__,
         'attributes': [x for x in dir(obj) if not callable(getattr(obj, x))],
         'methods': [x for x in dir(obj) if callable(getattr(obj, x))],
         'module': obj.__class__.__module__}

    return introspection_dict


number_info = introspection_info(10)
print(number_info)
