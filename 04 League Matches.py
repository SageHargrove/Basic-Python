####################################################################
# author: Sage Hargrove
# date: 10/20/2023
# description:
####################################################################
# A function to prompt the user for the number of teams in a league. It
# does not take any arguments and returns the result to the calling
# statement.
# A function that calculates the number of matches in a league. It
# receives a single numerical argument representing the number of teams
# in the league, and uses RECURSION to calculate the minimum number of
# matches required. It then returns the result to the calling statement.
# A function that prints out the final results. It receives two
# arguments that represent the number of teams and matches.
############################ MAIN #################################
# get the number of teams
def numberofteams():
    teams = int(input("How many teams are in this league? "))
    return teams
# calculate the number of matches
def calcmatch(teams):
    if teams  <= 1:
        return 0
    else:
        return (teams-1) + calcmatch(teams-1)
# print the results to the screen.
def results():
    print (f"A league of {teams} teams would require at least {n} matches")
teams = numberofteams()
n = calcmatch(teams)
results()
