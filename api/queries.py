from .models import d_product
from ariadne import convert_kwargs_to_snake_case


def listProduct_resolver(obj, info):
    try:
        products = [product.to_dict() for product in d_product.query.all()]
        response = {
            "success": True,
            "product": products
        }
    except Exception as error:
        response = {
            "success": False,
            "errors": [str(error)]
        }
    return response


def getProduct_resolver(obj, info, id_product):
    try:
        product = d_product.query.get(id_product)
        response = {
            "success": True,
            "product": product.to_dict
        }
    except AttributeError:
        response = {
            "success": False,
            "errors": ["Product matching {id} not found"]
        }

    return response
