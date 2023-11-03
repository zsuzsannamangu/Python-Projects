#Creating a class that utilizes the concept of abstraction
#Class has one abstract method and one regular method
#Creating child classes that define the implementation of tghe parent's abstract method
#Creating an object that utilizes both the parent and the child methods

#First we need to import "abstractmethod" from the abc module (Abstract Base Class)
from abc import ABC, abstractmethod

#created an abstract base class called "Vehicle" using the ABC module
class Vehicle(ABC):

    def numberOfSeats(self, number):
        print("You are a group of ",number)
    
    #"Vehicle" has an abstract method "doors" that needs to be implemented by its subclasses
    #A method becomes abstract when decorated with the @abstractmethod keyword
    @abstractmethod
    def seats(self, number):
        pass

class Coupe(Vehicle):
    #we override the abstract method "seats" of the class Vehicle
    def seats(self, number):
        print("This is a Mercedes CL-Class 2 door car and does not have {} seats.".format(number))

class Sedan(Vehicle):
    #we override the abstract method "seats" of the class Vehicle
    def seats(self, number):
        print("This is an Aston Martin Rapide 4 door car that have {} seats.".format(number))

obj = Coupe()
obj2 = Sedan()
obj.numberOfSeats(5)
obj.seats(5)
obj2.seats(5)
