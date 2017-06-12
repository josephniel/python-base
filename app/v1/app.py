from interface.base_app import BaseApp
from .views.public import PublicViews


class V1App(BaseApp):
    """This is an application class that inherits from the ``BaseApp``
    class containing the initialization of a blueprint and its
    retrieval (i.e. for use in the bootstrap process).
    """

    def __init__(self):
        super(V1App, self).__init__('v1.app')

        self._prepare_views()

    def _prepare_views(self):
        """This is a container function that collates all functions
        that contains the application views
        """

        PublicViews(self.route)
