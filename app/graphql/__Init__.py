from flask import Blueprint

graphql = Blueprint("graphql", __name__, url_prefix="graphql", static_folder="/static", template_folder="/templates")

from . import forms, routes
