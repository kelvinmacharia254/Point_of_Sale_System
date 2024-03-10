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

# *** The shop stocks various categories of product
Data storage strategy
# 1. Store all available categories of products(id, category_name)
# 2. Store all available products (id, product_name, description, category, unit_price)
# 3. Store stock levels for each product (id, product_name, stock_levels)
# 4. Record sales (id, quantity_sold, unit_price, total)

"""

import logging

logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt="%d-%b-%y %H:%M:%S")

def list_products():
    """
    List all available products
    :return:
    """
    pass


def add_product():
    """
    Add a product to the inventory
    """
    pass


def delete_product():
    """
    Delete a product from the inventory
    :return:
    """
    pass


def list_categories():
    """
    List all available product categories
    :return:
    """
    categories = read_file("categories.txt")
    print("Product Categories:")
    if len(categories) > 0:
        for i, category in enumerate(categories):
            print(str(i + 1) + "." + category.strip())
    else:
        print("No categories found")


def add_category():
    """
    Add a category to the inventory
    :return:
    """
    categories = "Flash drives\n"
    # categories = ['RAM\n', 'Storage\n', 'Monitors\n']
    write_to_file(categories, "categories.txt", mode="a")


def delete_category():
    """
    Delete a category from the inventory.

    """
    category_to_delete = "RAM\n"
    categories = read_file("categories.txt")
    print(categories)
    if category_to_delete in categories:
        while True:
            print("You are about to delete the '" + category_to_delete + "' category.")
            print("Are you sure you want to delete this category?")
            answer = input("[Y]es to delete | [N]o to cancel deletion.\n ")
            if answer.upper() == "Y":
                categories.remove(category_to_delete)
                print("You have successfully deleted the '" + category_to_delete + "' category.")
                write_to_file(categories, "categories.txt", mode="w")
                break
            elif answer.upper() == "N":
                print("You have cancelled the deletion.")
                break
            else:
                print("Invalid input entered.")

    else:
        print(f"There is no category '{category_to_delete}'.")


def restock():
    """
    Restock a product from the inventory
    :return:
    """
    pass


def sale():
    """
    Sale a product from the inventory
    :return
    """
    pass


def read_file(file_name):
    """
    Read a file or create new if it doesn't exist.
    :param file_name:
    :return: File_object or content of file
    """
    try:
        with open(file_name) as f:
            content_list = f.readlines()
            return content_list
    except Exception as e:
        logging.critical(f"{e}")
        file_content = open(file_name, mode='r')  # create file if non-existent
        return file_content


def write_to_file(file_contents, output_filename, mode):
    """
    Write a file or create new if it doesn't exist.
    :param file_contents: Content to write to the file
    :param output_filename:name of file
    :param mode:mode for opening the file
    returns: None
    """

    try:
        f = open(output_filename, mode)
    except Exception as e:
        logging.critical(f"{e}")
        f = open(output_filename, mode)  # create file if non-existent

    f.writelines(file_contents)
    f.close()


list_categories()

# add_category()
delete_category()

list_categories()
