####################################################################
# name: Sage Hargrove
# date: 10/04/23
# description: This program will use an individuals principal, annual percentage rate, and number of years to calculate compound 
# interest.
####################################################################
# A function that receives no arguments, prompts the user for their
# name, and returns that value to the calling statement.
# A function that receives a single argument (a string that describes a
# piece of data), prompts the user for that data, and then returns the
# data to the calling statement.
# A function that receives three arguments that represent the principal
# amount, annual compound interest rate, and the number of years, and
# returns the total amount after compound interest growth.
###################### MAIN #########################
# using the function(s) above as appropriate, complete the algorithm
# below.
# prompt the user for their name
# prompt the user for the principal amount, annual compound interest
# rate, and number of years
# Calculate the total amount
# Print out the final amount
def user():
    name = input("Please enter your name: ") # prompt the user for their name
    return name

def variables():
    principal = float(input("Please enter the principal: ")) # prompt the user for the principal amount
    interest = float(input("Please enter your annual percentage rate: ")) # prompt the user for the annual compound interest rate
    years = float(input("Please enter the number of years: ")) # prompt the user for the number of years
    return principal, interest, years

def final(principal, interest, years):
    total =  principal*(1 + interest/100)**years # Calculates the total amount
    total = round(total, 2) # Rounds the total amount
    return total

name = user()
principal, interest, years = variables()
total = final(principal, interest, years)
print(f"Hello {name}, the final amount after {years} years at {interest}% is ${total}")
