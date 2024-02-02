############################################################################
# name: Sage Hargrove
# date: 1/10/24
# description: This is a program that ComplexTest is inheriting the Complex class from, which involves
# operation overloading to allow functions to work with complex numbers.
###########################################################################

# Don't forget to name this file Complex.py and place it in the same
# folder as the provided ComplexTest.py file so that they can
# automatically find and use each other.

class Complex:
    # A constructor that takes two values for the real and imaginary
    # portions respectively. Default values for both parameters are 0.
    def __init__(self, real = 0, imaginary = 0):
        self.real = real
        self.imaginary = imaginary

    # Accessors and Mutators for the instance variables
    @property
    def real(self):
        return self._real
    @real.setter
    def real(self, newReal):
        self._real = newReal
    
    @property 
    def imaginary(self):
        return self._imaginary
    @imaginary.setter
    def imaginary(self, newImaginary):
        self._imaginary = newImaginary
    # Overloaded mathematical operators i.e. ==, +, -, *, /
    def __eq__(self, complexVal):
        if self.real == complexVal.real and self.imaginary == complexVal.imaginary:
            return True
        else:
            return False
        
    def __add__(self, complexVal):
        newReal = self.real + complexVal.real 
        newImaginary = self.imaginary + complexVal.imaginary
        return Complex(newReal, newImaginary)
    
    def __sub__(self, complexVal):
        newReal= self.real - complexVal.real
        newImaginary = self.imaginary - complexVal.imaginary
        return Complex(newReal, newImaginary)
    
    def __mul__(self, complexVal):
        newReal = self.real * complexVal.real - self.imaginary * complexVal.imaginary
        newImaginary = self.real * complexVal.imaginary + self.imaginary * complexVal.real
        return Complex(newReal, newImaginary)
    
    def __truediv__(self, complexVal):
        denominator = complexVal.real**2 + complexVal.imaginary**2
        newReal = (complexVal.real * self.real + complexVal.imaginary * self.imaginary) / denominator
        newImaginary = (complexVal.real * self.imaginary - complexVal.imaginary * self.real) / denominator
        return Complex(newReal, newImaginary)
    # Other functions e.g. reciprocal, conjugate, and __str__
    def reciprocal(self):
        denominator = (self.real ** 2 + self.imaginary ** 2)
        newReal = self.real / denominator
        newImaginary = - 1 * self.imaginary / denominator
        return Complex(newReal, newImaginary)
    
    def conjugate(self):
        return Complex(self.real, -self.imaginary)
    
    def __str__(self):
        if self.imaginary >= 0: 
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {-1 * self.imaginary}i"
