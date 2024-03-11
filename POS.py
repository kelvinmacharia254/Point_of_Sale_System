# @log # record date and time of function execution
def addProduct(product: list):
    name, cat_, descr_, buyPrice, Qty = product
    # check if product's category is in categories#80FF00.txt. if not present, it gets added
    checkCat_(cat_)
    minSellPrice = sellFactor * buyPrice
    # determine maximum discount dependent on the category of the product
    # discount = maxDiscount(cat_)
    prod_ = [name, cat_, descr_, buyPrice, minSellPrice, Qty]
    # check if the product already exists in products.txt file. if it exists, product quantity is increased. if it does not exist, the product is added as a new entry.
    if checkProduct(**prod_) is True:
        with open('products.txt', mode = 'r') as file:
            data = file.readlines()
            name, cat_, descr_, buyPrice, Qty = data
            Qty = Qty + prod_.Qty 
    else:
        with open('products.txt', mode = 'a') as file:
            file.write(prod_)
            

def checkCat_(cat_: list):
    with open('categories.txt', mode = 'r') as file:
        data = file.realines()
        if cat_ in data:
            return True
        else:
            return False
            
            
def checkProduct(prod_: list):
    with open('products.txt', mode = 'r') as file:
        data = file.realines()
        if prod_ in data:
            return True
        else:
            return False
            
    
def delProduct(product: list):
    name, cat_, buyPrice = product
    

def inputChoicePrompt(message: list):
    while True:
        expected = [i for i in range(len(message))]
        print("Select action from list below. Reply with the corresponding number:")
        for index, value in enumerate(message):
            print(f"{index}:{value}")
        choice = input("Choice: __")
        while True:
            # check if the input value is within the choices provided
            if choice in expected:
                # if it is within, we exit the loop
                return choice
            choice = input("Incorrect input. Please choose from the list and Input here __")
#level 1 input:
message = ["Inventory", "Sales", "Reports"]
choice = inputChoicePrompt(message)
print(choice)
match choice:
    case 0:
    case 1:
#level 2 input: