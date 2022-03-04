from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import d_product

@convert_kwargs_to_snake_case
def create_product_resolver(obj, info, name, standard_cost, list_price):
    # TODO
    pass