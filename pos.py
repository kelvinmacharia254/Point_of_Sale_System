"""
This is the implementation of Python Expert Computer shop.
Authors:
1. Caroline
2. Kelvin
3. Rogers

Key Functions
1. List categories and products available.
2. Delete or add product categories or products.
   Question: What happens if you delete a product category?
3. Product selling
4. Sale reports
5.
6.
"""

# imports
from pprint import pprint

# Global variables
# ********** The shop stocks various categories of products
product_categories = [
    'laptops', 'Printers', 'phones', 'micro-controllers'
]

"""
List of products with each product attribs stored as dictionary.
Possible improvements
- separate the products from stock levels.
"""
products = [
    {'product_name': 'hp omen', 'price': 150000, 'category': product_categories[0], 'description': 'black',
     'quantity': 10},
    {'product_name': 'Epson Printer', 'price': 50000, 'category': product_categories[1], 'description': 'Silver+white',
     'quantity': 4},
    {'product_name': 'Iphone 14', 'price': 209000, 'category': product_categories[2], 'description': 'Gold',
     'quantity': 30},
    {'product_name': 'Rasberry Pi 4', 'price': 35000, 'category': product_categories[3], 'description': 'black',
     'quantity': 11}
]


def list_products():
    """
    List all products.
    :return: products list and number of product type as dictionary.
    """
    return {'products': products, 'no_of_items': len(products)}


def add_product(product: dict) -> str:
    """
    Add product to list product global variable.
    Testing:
    1. Has all products attrs provide. Can you have Nulls
    2. Datatype of product and it's attrs
    3. Does the category exist
    3. Check if it is a Duplicate
    :param product:
    :return:
    """
    products.append(product)
    return f"product: {product['product_name']} successfully added"


def delete_product(product: dict) -> str:
    pass


def list_categories() -> list:
    """
    List all categories
    :return: category list
    """
    return product_categories


def add_category(category: str) -> str:
    """
    Add product category
    :param category:
    :return:
    """
    category.append(category)
    return f"category {category} successfully added"


def delete_category(category: list) -> str:
    category.remove(category)
    return f"category {category} deleted successfully added"


"""
# Add product.
#   Add a specific product. An example has been given
print("###Add product.####")
product = {}
product['product_name'] = 'arduino board'
product['price'] = 23000
product['category'] = product_category[3]
product['description'] = 'blue'
product['quantity'] = 73
product_message = add_product(product)
print(product_message)
#   list product to see update
products_information = list_products()
pprint(products_information['products'])
print(products_information['no_of_items'])
print("###End of add product.####")

print("\n")

# Add category
print("###Add category.####")
category_add_message = add_category('cables')
print(category_add_message)
category_add_message = add_category('storage')
#   list categories to see update
print(list_categories())
print("###End of add Category.####")

print("\n")

# Delete category
print("###Delete category.####")
category_delete_message = delete_category('storage')
print(category_delete_message)


"""
#   list categories
print("### category list ###")
print(list_categories())
print("\n")

#   list products
print("### products list ###")
products_information = list_products()
pprint(products_information)
