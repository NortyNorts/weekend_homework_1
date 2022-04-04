
# 1 create a function that returns the "name" from a dictionary in the pet shop test file
from pickle import APPEND


def get_pet_shop_name(shop): #This line creates the funtion and allows for one argument to be passed
    return shop["name"] #This line searches for the argument passed into "shop" for the dictionary string "name" and returns
    #the value from that dictionary item.

# 2 create a function that returns an integer from a dictionary in the pet shop test file
def get_total_cash(shop): #This line creates the funtion and allows for one argument to be passed
    return shop ["admin"]["total_cash"] #This line searches for the argument passed into "shop" for the dictionary string "admin" 
    #and then another string called "total_cash" and then returns the value from that dictionary item.

# 3 create a funtion that will add, or remove an integer from a dictionary in the pet shop
# test file
def add_or_remove_cash(shop, cash_amount): #This line creates the funtion and allows for one argument to be passed
    shop ["admin"]["total_cash"] += cash_amount #This line searches for the argument passed into "shop" for the dictionary string "admin" 
    #and then another string called "total_cash" and then returns the value from that dictionary item.

# 4
def get_pets_sold(shop):
    return shop["admin"] ["pets_sold"]

# 5
def increase_pets_sold(total_pets, pets_sold):
    total_pets ["admin"]["pets_sold"] += pets_sold

# 6
def get_stock_count(shop):
    return len(shop["pets"])

# 7
def get_pets_by_breed(shop, breed):
    pets = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    return pets

# 8 and 9
def find_pet_by_name(shop, check_name):
    for pet in shop["pets"]:
        if pet["name"] == check_name:
            return pet

# 12
def remove_pet_by_name(shop, pet_name):
        for pet in shop["pets"]:
            if pet["name"] == pet_name:
                shop["pets"].remove(pet)

# 11
def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

# 12
def get_customer_cash(customer_cash):
    total_cash = 0
    total_cash += customer_cash["cash"]
    return total_cash

# 13
def remove_customer_cash(customer, money):
    customer["cash"] -= money

# 14
def get_customer_pet_count(pets):
    return len(pets["pets"])

# 15
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

# Option 1, 2 , 3
# Can customer afford pet?
def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet ["price"]:
        return True
    else:
        return False

# Integration test 1
# Create function that removes customer cash and adds it to shop total cash,
# Increases pets sold
# Increases customer pet count
# 
def sell_pet_to_customer(shop, pet, customer):
    transaction_cost = 0
    transaction_cost += pet["price"]
    customer["cash"] -= transaction_cost
    shop ["admin"]["total_cash"] += transaction_cost



