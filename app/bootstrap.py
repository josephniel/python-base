from flask import Flask

from utils import import_submodules
from v1.views import ROUTES as v1_routes


class Bootstrap(object):
    """Container class that contains all the bootstrap
    processes needed to run the application.
    """

    APPLICATION_ROUTES_WHITELIST = {
        'v1': v1_routes,
    }

    def __init__(self):
        self.app = Flask(__name__)

    def ignite(self):
        """Function that triggers the start of the application
        which does the following:

            1. Loads the configuration from app/config/__init__.py
            2. Registers necessary application routes
            3. Publishes the application
        """
        self.app.config.from_object('config')
        self._register_routes()
        self._publish_application()

    def _register_routes(self):
        """Function that registers all the routes for the
        application versions present in the codebase
        """
        for package, routes in self.APPLICATION_ROUTES_WHITELIST.items():
            import_submodules(package)
            for route in routes:
                self.app.add_url_rule(
                    "/{package}{location}".format(
                        package=package,
                        location=route.location
                    ), view_func=route.view_func
                )

    def _publish_application(self):
        """Function that publishes the application on a particular
        host and port specified in the config plus additional
        flags (i.e. debug flag for dev purposes)
        """
        self.app.run(
            host=self.app.config.get('HOST', '0.0.0.0'),
            port=self.app.config.get('PORT', 5000),
            debug=self.app.config.get('DEBUG', False),
        )
