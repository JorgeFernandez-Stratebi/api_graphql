from .models import d_product, f_manufactures
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

@convert_kwargs_to_snake_case
def getProduct_resolver(obj, info, id_product):
    try:
        product = d_product.query.get(id_product)
        response = {
            "success": True,
            "product": product.to_dict()
        }
    except AttributeError:
        response = {
            "success": False,
            "errors": ["Product matching {id} not found"]
        }

    return response

def listManufactures_resolver(obj, info):
    try:
        manufactures = [manufacture.to_dict() for manufacture in f_manufactures.query.all()]
        response = {
            "success": True,
            "manufacture": manufactures
        }
    except Exception as error:
        response = {
            "success": False,
            "errors": [str(error)]
        }
    return response


@convert_kwargs_to_snake_case
def getManufacture_resolver(obj, info, id_manufacture):
    try:
        manufacture = f_manufactures.query.get(id_manufacture)
        response = {
            "success": True,
            "manufacture": manufacture.to_dict()
        }
    except AttributeError:
        response = {
            "success": False,
            "errors": ["Manufacture matching {id} not found"]
        }
    return response
