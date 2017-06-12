from flask import Flask

from v1.app import blueprint as v1_blueprint


class Bootstrap():
    """
    ---
    Container class that contains all the bootstrap
    processes needed to run the application.
    """

    def __init__(self):
        self.app = Flask(__name__)

    def ignite(self):
        """Function that triggers the start of the application"""

        self.app.config.from_object('config')

        self._register_blueprints()
        self._publish_application()

    def _register_blueprints(self):
        """Function that registers all the blueprints for
        the application versions present in the codebase"""

        self.app.register_blueprint(v1_blueprint)

    def _publish_application(self):
        """Function that publishes the application on a
        particular host and port specified in the config
        plus additional flags (i.e. debug flag for dev purposes)"""

        config = {
            'host': self.app.config.get('HOST', '0.0.0.0'),
            'port': self.app.config.get('PORT', 5000),
            'debug': self.app.config.get('DEBUG', False),
        }
        if __name__ == "__main__":
            self.app.run(**config)


"""
After all that's been prepared, it's time to light up 
the sky with your newly crafted application.
"""
Bootstrap().ignite()
