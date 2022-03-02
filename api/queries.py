from .models import d_product


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
