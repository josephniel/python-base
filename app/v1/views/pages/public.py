from flask import Response
from flask.views import MethodView
from . import route


@route("/", "sample")
class SampleView(MethodView):

    def get(self) -> Response:
        return "Hi"
