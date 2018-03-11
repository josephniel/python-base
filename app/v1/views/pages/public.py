from flask import Response, render_template
from flask.views import MethodView

from ..router import route


@route("/", "sample")
class SampleView(MethodView):

    def get(self) -> Response:
        return render_template(
            "hello.html"
        )
