#############################################################################
# author: Liam (Sage) Hargrove 
# date: 9/29/2023
# description: This program allows an individual to find their net income based on their gross income and tax rate.
#############################################################################





# A statement that prompts the user for their name
name = input("Please enter your name: ") # Get the individuals name

# Statements that prompt the user for their annual income and tax rate
gross = input(f"Hello {name}, what is your gross annual income? ") # Get the individuals gross income
gross = int(gross) # Change "gross" to be an int so that you can use it for math
tax = input("What is the percentage tax rate in your location? ") # Get the indivuals tax %
tax = float(tax) # Change "tax" to be an int so that you can use it for math

# Calculate the user's net income
net = gross*(1-(tax/100)) # Math to find the net income
net = int(round(net))
# Display the final output.
print(f"Well {name}, that means your net income is {net} ") # Tell the individiual their net income
