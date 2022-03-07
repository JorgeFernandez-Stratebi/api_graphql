from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import d_product
from datetime import datetime

@convert_kwargs_to_snake_case
def create_product_resolver(obj, info, id_product, name, standard_cost, list_price, product_line):
    try:
        date_time = datetime.now()
        product = d_product(id_product=id_product, name=name, standardCost=standard_cost, listPrice=list_price, productLine=product_line, updateDate=date_time)
        db.session.add(product)
        db.session.commit()
        response={
            "success": True,
            "product": product.to_dict()
        }
    except ValueError:
        response = {
            "success": False,
            "errors": ["Incorrect date and time format. Should be yyyy-mm-dd hh:mm:ss"]
        }

    return response


@convert_kwargs_to_snake_case
def update_product_resolver(obj, info, id_product, name, standard_cost, list_price, product_line):
    try:
        product = d_product.query.get(id_product)

        if product:
            if name:
                product.name = name
            if standard_cost:
                product.standardCost = standard_cost
            if list_price:
                product.listPrice = list_price
            if product_line:
                product.productLine = product_line
            product.updateDate = datetime.now()

        db.session.add(product)
        db.session.commit()

        response = {
            "success": True,
            "product": product.to_dict()
        }

    except AttributeError:
        response = {
            "success": False,
            "errors": ["Product matching id {id_product} not found"]
        }
    except ValueError:
        response = {
            "success": False,
            "errors": ["Incorrect date and time format. Should be yyyy-mm-dd hh:mm:ss"]
        }

    return response


@convert_kwargs_to_snake_case
def delete_product_resolver(obj, info, id_product):
    try:
        product = d_product.query.get(id_product)
        db.session.delete(product)
        db.session.commit()

        response = {
            "success": True,
            "product": product.to_dict()
        }
    except AttributeError:
        response = {
            "success": False,
            "errors": "Product not found"
        }

    return response