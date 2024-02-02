####################################################################
# author: Sage Hargrove
# date: 11/10/23
# description: 
####################################################################
# Lines to make the program look nice.
dash = "-"
line1 = dash * 60
equal = "="
line2 = equal * 60
# A function to print out the introduction to the program. It does not
# take any arguments or return any results.
dash = "-"
line = dash * 60
def intro():
    print(line1)
    print("Welcome to Cyber Groceries (v2)")
    print(line1)
# A function that prompts the user for the number of items that the
# store carries. It does not take any arguments but it returns the
# number of items to the calling statement.
def get_amount():
    amount = int(input("How many items does the store carry? "))
    return amount
# A function that creates a list of item names by repeatedly prompting
# the user for item names. It takes an argument representing the
# number of items, and returns a single list containing the item
# names.
def get_groceries(amount):
    groceries = []
    n = amount
    for n in range (0, amount, 1):
        names = input(f"What is item number {n+1}? ")
        groceries.append(names)
    return groceries
# A function that creates a list of prices by repeatedly prompting the
# user for the prices for different items. It takes the list of
# item names as a single argument, and then returns a single list
# containing the prices for each of the items.
def get_prices(groceries):
    prices = []
    l = len(groceries)
    n = 0
    for n in range(0, l, 1):
        money = float(input(f"What is the price of {groceries[n]}? "))
        prices.append(money)
    return prices
# A function that creates a list that contains the number of units that
# were sold of each of the items in the store. It takes a single
# argument i.e. the list of item names, and after repeatedly asking the
# user for item amounts, returns the list of item units that were sold.
def get_item_amounts(groceries):
    item_amounts = []
    l = len(groceries)
    n = 0
    for n in range(0, l, 1):
        items = int(input(f"How many units of {groceries[n]} were sold today? "))
        items = round((items),2)
        item_amounts.append(items)
    print(line1)
    return item_amounts
# A function that prints out the summary table. It takes 3 arguments
# i.e. the list containing the item names, the list containing the item
# prices, and the list containing the item amounts. It uses these 3
# arguments to create a 4 column table that contains the name, unit
# price, number of units sold, and total amount made from that unit for
# each item. It does not return any arguments.
def summary(groceries, prices, item_amounts):
    print ("Item\tUnit Price\tNumber\tTotal Cost")
    print(line1)
    l = len(groceries)
    total_cost = []
    n = 0
    for n in range (0, l, 1):
        costs = float(prices[n]*item_amounts[n])
        total_cost.append(costs)
    n = 0   
    for n in range (0, l, 1):
        print(f"{groceries[n]}\t${prices[n]:.2f}\t\t{item_amounts[n]}\t${total_cost[n]:.2f}")
    print(line2)
######################### MAIN #####################################
# In the space below, use the functions defined above to solve the
# outlined problem.
####################################################################
# print out the introduction
intro()
# Prompt the user for the appropriate information
amount = get_amount()
groceries = get_groceries(amount)
prices = get_prices(groceries)
item_amounts = get_item_amounts(groceries)
# Print out items and their costs.
summary(groceries, prices, item_amounts)