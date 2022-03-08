from .models import d_product, inventory
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
        print(product)
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


def listInventory_resolver(obj, info):
    try:
        inventory_list = [element.to_dict() for element in inventory.query.all()]
        response = {
            "success": True,
            "inventory": inventory_list
        }
    except Exception as error:
        response = {
            "success": False,
            "errors": [str(error)]
        }
    return response


@convert_kwargs_to_snake_case
def getInventory_resolver(obj, info, id_product):
    try:
        inv_result = inventory.query.get(id_product)
        print(inv_result.to_dict())
        response = {
            "success": True,
            "inventory": inv_result.to_dict()
        }
    except AttributeError:
        response = {
            "success": False,
            "errors": ["Product matching {id} not found"]
        }
    return response
