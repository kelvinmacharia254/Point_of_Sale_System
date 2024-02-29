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

# ********** The shop stocks various categories of product
# Data storage strategy
# 1. Store all available categories of products(id, category_name)
# 2. Store all available products(id, product_name, description,category, unit_price)
# 3. Store stock levels for each product(id, product_name, stock_levels)
# 4. Record sales(id, quantity_sold, unit_price, total)


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
    for i, category in enumerate(categories):
        print(str(i + 1) + "." + category.strip())


def add_category():
    """
    Add a category to the inventory
    :return:
    """
    category = "laptops\n"
    write_to_file(category, "categories.txt", mode="a")
    pass


def delete_category():
    """
    Delete a category from the inventory
    """
    category_to_delete = "headsets\n"
    categories = read_file("categories.txt")
    print(categories)
    if category_to_delete in categories:
        while True:
            print("You are about to delete the '" + category_to_delete+"' category.")
            print("Are you sure you want to delete this category?")
            answer = input("[Y]es to delete | [N]o to cancel deletion.\n ")
            if answer.upper() == "Y":
                categories.remove(category_to_delete)
                print("You have successfully deleted the '" + category_to_delete+"' category.")
                write_to_file(categories, "categories.txt", mode="w")
                break
            elif answer.upper() == "N":
                print("You have cancelled the deletion.")
                break
            else:
                print("Invalid input entered.")

    else:
        print("There is no such category.")


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
    """Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """

    with open(file_name) as f:
        content_list = f.readlines()
        return content_list


def write_to_file(file_contents, output_filename, mode):
    """Writes the first line of a string to a file.

    [IMPLEMENT]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """

    content = file_contents
    f = open(output_filename, mode)
    if mode == "a":
        f.write(content)
    else:  # modes = "w"
        print(content)
        f.writelines(content)


list_categories()

# add_category()
delete_category()

list_categories()
