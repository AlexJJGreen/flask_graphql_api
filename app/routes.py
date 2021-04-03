from flask import current_app as app
from flask_graphql import GraphQLView
from app.graphql_logic.schema import schema, Cereal
from app.database_logic.models import db

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)

@app.teardown_appcontext
def session_close(exception=None):
    db.session.remove()


@app.route("/")
@app.route("/index")
def index():
    cereals = Cereal.query.all()
    return render_template("index.html", cereals=cereals)