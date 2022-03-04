from api import db


class d_product(db.Model):
    id_product = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    standardCost = db.Column(db.Numeric)
    listPrice = db.Column(db.Numeric)
    productLine = db.Column(db.String)

    prod_line_complete = {"R ": "Road", "M ": "Mountain", "T ": "Touring", "S ": "Standard"}

    def to_dict(self):
        return {
            "id_product": self.id_product,
            "name": self.name,
            "standard_cost": float(self.standardCost),
            "list_price": float(self.listPrice),
            "product_line": self.prod_line_complete.get(self.productLine)
        }


class f_manufactures(db.Model):
    id_manufacture = db.Column(db.Integer, primary_key=True)
    id_product = db.Column(db.Integer)
    REALCOST = db.Column(db.Numeric)
    QUANTITY = db.Column(db.Integer)

    def to_dict(self):
        if self.REALCOST is None:
            self.REALCOST = 0

        if self.QUANTITY is None:
            self.QUANTITY = 0
        return {
            "id_manufacture": self.id_manufacture,
            "id_product": self.id_product,
            "real_cost": float(self.REALCOST),
            "quantity": self.QUANTITY
        }
