from flask import Blueprint


blueprint = Blueprint('v1.app', __name__)


@blueprint.route("/")
def hello():
    return "Hello!"
