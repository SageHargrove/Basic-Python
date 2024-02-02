# operators and output
'''
Create two integer values called "num1" and "num2". The first variable, num1, should be
set to 56 and the second variable, num2, should be set to 89. Create a third variable 
called "num3" and set it equal to num1 times num2. Print the value of num3.

Time Taken (in mins): 1
Difficulty Rating (1 to 5): 1
'''
num1 = 56
num2 = 89
num3= num1*num2
print(num3)





# if statements and input
'''
Ask the user to enter a number and save the value they entered into a variable called "number".
Using an if statement, if the value in number is less than 10, print out "number is less than 10".
If the value is equal to 10, print out "number is 10". Otherwise print out "number is greater than 10"

Time Taken (in mins): 3
Difficulty Rating (1 to 5): 2
'''
number = int(input("Please enter a number: "))
if number < 10:
    print("number is less than 10")
elif number == 10:
    print("number is 10")
else:
    print("number is greater than 10")
'''
  
  
# loops
''
Use a while loop to figure out the value of 5 factorial (i.e. 5 * 4 * 3 * 2 * 1).
Print out the result

Time Taken (in mins): 1
Difficulty Rating (1 to 5): 1
'''
n = 1
x = 0
while n <= 5:
    x = n*(n-1) # multiplying the number by its previous term repeatedly, until it is equal to 5
    n+=1
print(x)






# functions
'''
Create a function called "getNumber" that will ask the user to "enter a number".
This function returns what the user entered after converting it to an integer.
In the main section, call this function and save what it returns into a variable
called "number". Lastly, print out the number.

Time Taken (in mins): 2
Difficulty Rating (1 to 5): 1
'''
def getNumber():
    x = int(input("enter a number"))
    return x
number = getNumber()
print(number)






# functions again
'''
Create a function called "printMsg" that takes in a parameter called "msg". This
function will print "Your message is: " followed by the message sent to the function (i.e.
the parameter msg).

Create another function called "addFive" that takes in a parameter called "num". This
function returns the result of adding 5 to the parameter it was given.

Create another function called "getRandom" that returns a random number from 0 to 5 inclusively.
In the main section, call the printMsg function once (giving it whatever message you want).

Also call the addFive function 3 times (with different values each time) and print out the value it 
returns each time. 

Call the getRandom function once, save what it returns into a variable called "value"
and print out that value.

Time Taken (in mins): 5
Difficulty Rating (1 to 5): 3
'''
def printMsg(msg): 
    print(f"Your message is: {msg}")

def addFive(num):
    x = num+5
    return x

from random import randint
def getRandom():
    x = randint(0, 5)
    return x


printMsg("Yo!")

x = addFive(5)
y = addFive(15)
z = addFive(40)
print(x,y,z)

value = getRandom()
print(value)



