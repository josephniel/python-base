from interface.base_app import BaseApp


class V1App(BaseApp):
    """This is an application class that inherits from the ``BaseApp``
    class containing the initialization of a blueprint and its
    retrieval (i.e. for use in the bootstrap process).
    """

    def __init__(self):
        super(V1App, self).__init__('v1.app')
        self._define_routes()

    def _define_routes(self):
        @self.route("/")
        def hello():
            return "Hello!"
