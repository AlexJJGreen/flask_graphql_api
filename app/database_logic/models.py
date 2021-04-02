from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cereal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    mfr = db.Column(db.String(1))
    calories = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    sodium = db.Column(db.Integer)
    fiber = db.Column(db.Integer)
    carbo = db.Column(db.Integer)
    sugars = db.Column(db.Integer)
    potass = db.Column(db.Integer)
    vitamins = db.Column(db.Integer)
    shelf = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    cups = db.Column(db.Float(precision=5))
    rating = db.Column(db.Float(precision=5))


#name	mfr	type	calories	protein	fat	sodium	fiber	carbo	sugars	potass	vitamins	shelf	weight	cups	rating
