######################################################################
# name: Sage Hargrove
# date: 1/24/24
# desc: This program will use classes and subclasses to add even more depth to the patients. There is 2 subclasses to the patient
# class, and an additional subclass for each of those subclasses. This will allow the program to give the user significantly
# more information than the basic patient class was able to.
####################################################################

# A patient class. A patient has a name, age and weight. Only the name
# and age are provided as arguments for the constructor. On top of
# accessors and mutators for those variables, the patient class also has
# an increaseAge function that increases the age by 1.
class Patient:
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age
        self.weight = 150 # weight will default to 150
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, newName):
        self._name = newName
    
    @property
    def age(self):
        return self._age 
    
    @age.setter
    def age(self, newAge):
        if (newAge > 0): # age cannot be negative, and if it is given as such it will default to 0
            self._age = newAge
        else: 
            self._age = 0
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, newWeight):
        if (newWeight <= 1400 and newWeight >= 0): # must be between 0 and 1400, inclusive
            self._weight = newWeight

    def increaseAge(self): # function increases age by 1, ex birthday
        self.age += 1
# An In class which is a subclass of the Patient class and refers to an
# in-patient. An in-patient also contains a "stay" instance variable 
# that stores the number of days that that patient will stay in the
# hospital. Its constructor receives the name, age and stay duration as
# arguments. On top of appropriate accessors and mutators, the In class
# also has a __str__ function to define how an In object would be printed.
class In(Patient):
    def __init__(self, name, age, stay):
        super().__init__(name, age)
        self.stay = stay

    @property
    def stay(self):
        return self._stay
    
    @stay.setter
    def stay(self, newStay):
        if (newStay > 0): 
            self._stay = newStay

    def __str__(self):
        return f"(IN-\t{self.name}\t{self.age}\t{self.weight}\t{self.stay}"

# An Out class, which is a subclass of the Patient class and refers to
# an out-patient. An outpatient receives the name and age as arguments
# to its constructor. It also has a __str__ function that defines how an
# Out object would be printed.
class Out(Patient):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f"(OUT-\t{self.name}\t{self.age}\t{self.weight}"
# An ICU class which is a subclass of the In class and refers to a
# patient in the ICU. The ICU class receives the name and age as
# arguments to its constructor. It also has a class variable called days
# with the value 5 stored in it. This class variable is used to
# determine what the stay of the patient will be.
class ICU(In):
    days = 5
    def __init__(self, name, age):
        super().__init__(name, age, ICU.days)
# A CheckUp class which is a subclass of the Out class and refers to a
# patient who is getting a checkup at the hospital. It receives the name
# and age as arguments for its constructor.
class CheckUp(Out):
    def __init__(self, name, age):
        super().__init__(name, age)