##########################################################################
# author:   Sage Hargrove
# date:    12/11/23
# desc:   i forgot thats so lame
#########################################################################
from random import randint, seed
SHOWLIST = True 	# a boolean to determine whether to show the list
MIN = 0			# the smallest random number that can be created.
MAX = 1000		# the largest random number that can be created.



# A function that prompts the user for two pieces of information i.e.
# the size of the list they want to create, and the seed that will be
# used for the list creation. It then returns both pieces of information to the
# calling statement.
def userInputs():
    listSize = int(input("How big a list do you want to create? "))
    seedValue = int(input("What seed should be used for its creation? "))
    return listSize, seedValue

# A function that prints out a list. It receives two pieces of data. The
# first is a string representing the name of the list. The second is a
# list containing all the relevant data. It proceeds to print out the
# name, and then all the elements of the data separated using a tab
# space. Both the name and the entire list are printed on a single line.
def print_list(listName, listData):
    print(listName, end = "\t")
    for digit in listData:
        print(digit, end="\t")
    print()

# A function that creates the list of random numbers. It receives two
# arguments: one for the size of list to be created, and another for the
# seed that will be used to create the list. The function creates the
# list using the global variables MIN and MAX to form a bound for the
# kinds of numbers that are added to the list. The list is then returned
# to the calling statement.
def theList(listSize, seedValue):
    seed(seedValue)
    randList = [randint(MIN, MAX) for _ in range(listSize)]
    return randList

# A function that recieves a list of numbers and returns another list
# containing the frequency of the lists Most Significant Digits (MSD). The
# list created by the function has 10 elements with each value
# corresponding to a different possible MSD i.e. the value in index 0
# shows the number of values in the original number list that have 0 as
# their most significant digit; the value in index 1 shows the number of
# values with 1 as their MSD; and so on and so forth. This 10 element
# list is returned to the calling statemet.
def findMSD(randList):
    msd_count = [0] * 10
    for num in randList:
        msd_str = str(num)   #    char in vhar for list
        msd = int(msd_str[0])
        msd_count[msd] += 1
    return msd_count
# Similar to the function above, a function that recieves a list of
# numbers, and returns another list of 10 elements where each element
# represents the frequency of a specific Least Significant Digit in the
# original list.
def findLSD(randList):
    lsd_count = [0] * 10
    for num in randList:
        lsd_str = str(num)
        lsd = int(lsd_str[-1])
        lsd_count[lsd] += 1
    return lsd_count
###################################### MAIN ############################
# using the functions defined above:
#   prompt the user for the size of the list to be created as well as the seed.
listSize, seedValue = userInputs()
#   create the list of random numbers
randList = theList(listSize, seedValue)
#   If SHOWLIST is selected, print out the list of numbers
if SHOWLIST == True:
    print("Original List:")
    print(randList)
#   print the head of the table which just shows the numbers 0-9
print("-----------------------------------------------------------------------------------")
print(end = "\t")
for digit in range(10):
    print(digit, end = "\t")
print()
print("-----------------------------------------------------------------------------------")
#   Calculate the MSD and LSD, and print out their statistics.
msd_count = findMSD(randList)
lsd_count = findLSD(randList)
print_list("MSD", msd_count)
print_list("LSD", lsd_count)