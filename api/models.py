from api import db


class Product(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    standardCost = db.Column(db.Integer)
    listPrice = db.Column(db.Integer)


class Manufacture(db.Model):
    id_manufacture = db.Column(db.Integer, primary_key=True)
    id_product = db.Column(db.Integer)
    REALCOST = db.Column(db.Float)
    QUANTITY = db.Column(db.Integer)
