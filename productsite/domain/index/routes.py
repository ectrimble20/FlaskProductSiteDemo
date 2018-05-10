from flask import Blueprint, render_template

index = Blueprint('index', __name__)


@index.route("/", methods=["GET"])
@index.route("/index", methods=["GET"])
@index.route("/home", methods=["GET"])
def index_page():
    return render_template('index.html', title="Index")
