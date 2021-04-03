from flask import render_template
from flask import current_app as app
from app.database_logic.models import Cereal

@app.route("/")
@app.route("/index")
def index():
    cereals = Cereal.query.all()
    return render_template("index.html", cereals=cereals)