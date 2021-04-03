from flask import Blueprint

graphql_logic = Blueprint("graphql_logic", __name__, url_prefix="/graphql_logic", static_folder="/static", template_folder="/templates")

from . import schema
