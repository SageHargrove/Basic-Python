####################################################################
# author: Sage Hargrove
# date: 11/03/23
# description:This program will take the input of a grocery list and their costs, then output the cheapest
# item, the most expensive item, and the total cost of all of the items.
####################################################################
# lines for making the program look nice
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
    print("Welcome to Cyber Groceries")
    print(line1)
# A function that prompts the user for the number of items that the
# customer is buying. It does not take any arguments but it returns the
# number of items being bought to the calling statement.
def get_amount():
    amount = int(input("How many items is the customer buying? "))
    return amount
# A function that creates a list of item names by repeatedly prompting
# the user for product names. It takes an argument representing the
# number of items, and returns a single list containing the product
# names.
def get_groceries(amount):
    groceries = []
    n = 0
    while n < amount:
        n += 1
        names = input(f"What is item number {n}? ")
        groceries.append(names)
    return groceries
# A function that creates a list of prices by repeatedly prompting the
# user for the prices for different products. It takes the list of
# product names as a single argument, and then returns a single list
# containing the prices for each of the products.
def get_prices(groceries):
    prices = []
    n = 0
    while n < len(groceries):
        money = float(input(f"What is the price of {groceries[n]}? "))
        prices.append(money)
        n += 1
    print(line1)
    return prices
######################### MAIN #####################################
# In the space below, use the functions defined above to solve the
# outlined problem.
####################################################################
# print out the introduction
intro()
# Prompt the user for the appropriate information
amount = get_amount()
# Print out items and their costs.
groceries = get_groceries(amount)
prices = get_prices(groceries)
print(groceries)
print(prices)
print(line1)
# Figure out what the cheapest and most expensive items are as well as
# what the total cost would be.
min_value = prices.index(min(prices))
max_value = prices.index(max(prices))
total = sum(prices)
# Print out the information on cheapest, most expensive and total cost.
print(f"The cheapest item is {groceries[min_value]}")
print(f"The most expensive item is {groceries[max_value]}")
print(total)
print(line2)