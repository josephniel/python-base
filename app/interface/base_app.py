from flask import Blueprint


class BaseApp(object):
    """This is a parent class in which application classes should
    inherit from. This parent class contains the following:

        1. The blueprint to be used for bootstrapping the application
        2. The routes decorator that wraps the application routes decorator
    """

    def __init__(self, blueprint_name):
        self.blueprint = Blueprint(blueprint_name, __name__)

    def get_blueprint(self):
        """Gets the blueprint of the application"""
        return self.blueprint

    def route(self, route):
        """Wrapper for the application routes decorator"""
        return self.blueprint.route(route)
