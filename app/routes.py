from collections import namedtuple


def route(routes, location, name):
    def wrapper(cls):
        class_route = namedtuple('ClassRoute', ['location', 'view_func'])
        routes.append(class_route(
            location=location, view_func=cls.as_view(name)
        ))
        return cls
    return wrapper
