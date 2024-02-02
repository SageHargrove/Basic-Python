##########################################################################
# name: Sage Hargrove
# date: 10/27/23
# description: Compare the population of two different countries based on their
# initial population and annual growth rate, with user specified intervals and
# total amount of years.
#########################################################################
# A function that prints out the introduction to the program. It doesn't
# take any arguments and does not return any results.
def intro():
    print("This program will compare the populations of two different countries over time")
# A function that prompts the user for the name of the country. It takes
# in a number that is used in the prompt as an argument. It then returns
# the name of the country.
def get_countries(n):
    countries = input(f"What is the name of country #{n}: ")
    return countries
# A function that prompts the user for the current population of a
# country. It takes the name of the country as an argument, and then
# returns the resulting population. The function also carries out range
# checking to make sure the value inputed by the user is valid (i.e. not
# negative)
def get_pop(countries):
    pop = int(input(f"What is the current population of {countries}? "))
    while pop <= 0:
        print("That doesn't seem right. Please enter a positive number")
        pop = int(input(f"What is the current population of {countries}? "))
    return pop
# A function that prompts the user for the population growth rate of a
# country. It takes in the name of the country as an argument and then
# returns a value growth rate. It also carries out range checking to
# make sure that the result is not an unrealistic growth rate i.e. rate
# should be between -5 and 10 inclusive.
def get_growth(countries):
    growth = float(input(f"What is the annual population growth rate of {countries}? "))
    while growth >= 10:
        print("That doesn't seem right. Please enter a value within the range [-5, 10]")
        growth = float(input(f"What is the annual population growth rate of {countries}? "))
    while growth <= -5:
        print("That doesn't seem right. Please enter a value within the range [-5, 10]")
        growth = float(input(f"What is the annual population growth rate of {countries}? "))
    return growth
# A function that prompts the user for the number of years to show in
# the resulting table. The function doesn't take any arguments but
# returns a result. It is also in charge of range checking to make sure
# that the number of years is not less than 1.
def get_years():
    years = int(input(f"How many years of comparison should the table show? "))
    while years < 1:
        print("That doesn't seem right. Please enter a positive number")
        years = int(input(f"How many years of comparison should the table show? "))
    return years

# A function that prompts the user for the duration of the interval in
# the table i.e. how many years between each successive row of the
# resulting table. It doesn't take any arguments and does range checking
# to make sure that the user doesn't enter a value less than 1.
def get_interval():
    interval = int(input(f"How many years should the intervals be? "))
    while interval < 1:
        print("That doesn't seem right. Please enter a positive number")
        interval = int(input(f"How many years should the intervals be? "))
    return interval

# A function that calculates the population given an intial population,
# a growth rate, and the time. It takes 3 arguments (population, growth
# rate and time) and returns the resulting population.
def finalpop(pop, growth, years):
    final = int(pop*(1+(growth/100))**years)
    return final
# A function to print out the header o  f the table. It takes two
# arguments i.e. the country names, and then prints out the formatting
# lines as well as the first row seen at the top of the table.
def header(country1, country2):
    dash = "-"
    line = dash * 70
    print(line)
    print(f"Years \t \t \t  {country1} \t \t \t {country2}")
    print(line)
# A function to print out the rest of the table row by row. It receives
# 6 arguments: both country populations, both country rates, the
# duration of the analysis and the interval between each row. It then
# relies on calculate population function to calculate the upopulation
# values for each row and print them out in order.
def body(pop1, pop2, growth1, growth2, years, interval):
    dash = "-"
    line = dash * 70
    total_interval = 0
    while total_interval <= years:
        pop1f = finalpop(pop1, growth1, total_interval)
        pop2f = finalpop(pop2, growth2, total_interval)
        format(print(f"{total_interval:,} \t \t \t {pop1f:,} \t \t \t {pop2f:,}"))
        total_interval += interval
    print(line)
    ############### MAIN ##################################
# print the introduction
intro()
# Get the country names
country1 = get_countries(1)
country2 = get_countries(2)
# Get the country initial populations
pop1 = get_pop(country1)
pop2 = get_pop(country2)
# get the country population growth rates
growth1 = get_growth(country1)
growth2 = get_growth(country2)
# get the analysis details e.g. the duration and the interval
years = get_years()
interval = get_interval()
# Print out the table
header(country1, country2)
body(pop1, pop2, growth1, growth2, years, interval)