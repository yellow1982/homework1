def introspection_info(obj):
    introspection_dict = \
        {'type': type(obj).__name__,
         'attributes': dir(obj),
         'methods': [x for x in dir(obj) if callable(getattr(obj, x))],
         'module': obj.__class__.__module__}

    return introspection_dict


number_info = introspection_info(10)
print(number_info)
