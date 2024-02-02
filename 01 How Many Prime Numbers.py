#######################################################################
# author: Sage Hargrove
# date: 12/6/2023
# desc: This program will give all prime numbers below a user specified value
########################################################################

# A function to prompt the user for a number and return that value to
# the calling statement.
def primeValue():
    value = int(input("What limit are you interested in? "))
    return value
# A function that receives a number and tests that number to see whether
# it is prime or not. It returns the boolean response to the calling
# statement.
def primeTest(value):
    if value <= 1:
        return False
    for i in range (2, value):
        if value % i == 0:
            return False
    return True

################### MAIN ######################################
# Using the functions declared above, ask the user for a number, then
# create a list of all the prime numbers less than that number. Proceed
# to print out the relevant information related to that list.
value = primeValue()
primeList = []
for prime in range(2, value):
    if primeTest(prime):
        primeList.append(prime)
print(f"There are {len(primeList)} prime numbers less than {value}")
print(primeList)