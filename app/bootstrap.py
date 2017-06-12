from flask import Flask

from v1.app import V1App


class Bootstrap(object):
    """Container class that contains all the bootstrap
    processes needed to run the application.
    """

    APPLICATION_WHITELIST = [
        V1App(),
    ]  # type: List[object]

    def __init__(self):
        self.app = Flask(__name__)

    def ignite(self):
        """Function that triggers the start of the application
        which does the following:

            1. Loads the configuration from app/config/__init__.py
            2. Registers necessary application blueprints
            3. Publishes the application
        """
        self.app.config.from_object('config')
        self._register_blueprints()
        self._publish_application()

    def _register_blueprints(self):
        """Function that registers all the blueprints for the
        application versions present in the codebase
        """
        for application in self.APPLICATION_WHITELIST:
            self.app.register_blueprint(application.get_blueprint())

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
