#############################################################
# author: Sage Hargrove
# date: 12/18/23   
# desc: This program will make use of classes, in order to allow it to be used in a much bigger program and setting
# the patient's name, age, and weight.
#############################################################

# The patient class has a name, age, and weight. Only the name and age
# are provided as arguments to the constructor. The weight is set to 150
# by default for all objects. A Patient also has an increaseAge function
# that increases the age by 1.
class Patient:
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age
        self.weight = 150
    
    # getters/setters
    @property
    def age(self):       # underscore in front of name to prevent
        return self._age # recursion
    
    @property
    def weight(self):
        return self._weight

    # setters/mutators
    @age.setter
    def age(self, newAge):
        if (newAge > 0):
            self._age = newAge
        else: 
            self._age = 0
        
    @weight.setter
    def weight(self, newWeight):
        if (newWeight < 1400 and newWeight > 0):
            self._weight = newWeight

    def increaseAge(self): # function increases age by 1, ex birthday
        self.age += 1



################################################################
#****    DO NOT MODIFY ANYTHING BELOW THIS POINT!    ****
################################# MAIN #########################

# Create three patient objects and print them out
p1 = Patient("Ben Dover", 22)
p2 = Patient("Helen Hywater", 16)
p3 = Patient("Amanda Lynn", 45)

print ("\tName\t\tAge\tWeight")
print ("-" * 40)
print ("p1:\t{}\t{}\t{}".format(p1.name, p1.age, p1.weight))
print ("p2:\t{}\t{}\t{}".format(p2.name, p2.age, p2.weight))
print ("p3:\t{}\t{}\t{}".format(p3.name, p3.age, p3.weight))
print ("-" * 40)

# Change their ages and print them out
p1.age = -5
p2.age = 100
p3.increaseAge()
p3.increaseAge()

print ("p1:\t{}\t{}\t{}".format(p1.name, p1.age, p1.weight))
print ("p2:\t{}\t{}\t{}".format(p2.name, p2.age, p2.weight))
print ("p3:\t{}\t{}\t{}".format(p3.name, p3.age, p3.weight))
print ("-" * 40)

# Change other instance variables and print them out
p1.weight = 2000
p2.name = "Justin Thyme"
p2.weight = 220
p3.weight = -50

print ("p1:\t{}\t{}\t{}".format(p1.name, p1.age, p1.weight))
print ("p2:\t{}\t{}\t{}".format(p2.name, p2.age, p2.weight))
print ("p3:\t{}\t{}\t{}".format(p3.name, p3.age, p3.weight))
print ("-" * 40)
