####################################################################
# author: Sage Hargrove
# date:10/13/2023
# description: This program will find the approximate area of the function "3x^3 - 2x^2" between "a" and "b" with increasing
# accuracy depending on how low of a number you make your delta value.
####################################################################
# A function that is in charge of prompting the user for any input they
# give. It receives an argument representing the required data, prompts
# the user for that data, and then returns it to the calling statement.
def userinputs(var):
    inputs = float(input(f"What is the value of {var}: "))
    return inputs
# A function that is in charge of printing out the introductory
# statement(s) for the program.
def intro():
    print("The program will calculate the integral of the function 3x^3 - 2x^2 between user defined limits: a and b")

# A function that prints out the statement about the accuracy of delta.
def accdel():
    print("The accuracy of this calculation depends on the value of delta that you use")
    return True
# A function to evaluate the given mathematical formula at a given
# point. It takes a numerical argument that represents x, and returns
# the result of f(x).
def f(x):
    y = float(3 *(x)**3 - 2 *(x)**2)
    return y
# A function that calculates an approximation of the integral of f(x)
# using the riemann sum. It takes three arguments that represent the
# lower limit, the upper limit, and the delta value. It then returns the
# integral approximation as a result to1 the calling statement.
def riemann_sum(a, b, delta):
    x_val = a
    sum_area = 0
    while x_val < b:
        area = (delta * f(x_val))
        sum_area += area
        x_val+= delta
    return sum_area
########################### MAIN ##################################
# In the space below, use the functions defined above to solve the
# problem.
###################################################################
intro() # Print the introductory statements of the program
a = userinputs("a") # Prompt the user for the lower limit
b = userinputs("b") # Prompt the user for the upper limit
accdel() # Print the statements about delta
delta = userinputs("delta") # Prompt the user for the delta value
sum_area = riemann_sum(a, b, delta) # Calculate the integral approximation
print(f"The intelgral over the provided limits is {sum_area}") # Print out the result.

