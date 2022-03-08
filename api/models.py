from api import db


class d_product(db.Model):
    id_product = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    standardCost = db.Column(db.Numeric)
    listPrice = db.Column(db.Numeric)
    productLine = db.Column(db.String)
    updateDate = db.Column(db.DateTime)

    prod_line_complete = {"R ": "Road", "M ": "Mountain", "T ": "Touring", "S ": "Standard"}

    def to_dict(self):
        return {
            "id_product": self.id_product,
            "name": self.name,
            "standard_cost": float(self.standardCost),
            "list_price": float(self.listPrice),
            "product_line": self.prod_line_complete.get(self.productLine),
            "update_date": str(self.updateDate)
        }


class inventory(db.Model):
    id_product = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id_product": self.id_product,
            "amount": self.amount
        }
