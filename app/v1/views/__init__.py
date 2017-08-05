from routes import route as base_route

ROUTES = []


def route(location, name):
    return base_route(ROUTES, location, name)
