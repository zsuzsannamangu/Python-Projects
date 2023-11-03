#Here I create a class that uses encapsulation
#This class makes use of a private attribute and a protected attribute

#Creating a class
class Car:
    #Creating two protected attributes of the class:
    _make = "Honda"
    _model = "Civic"
    __idnumber= "2334kdkd"

    #creating a function
    def _MakeAndModel(self):
        #this function is using the protected attributes of the Car class
        print("Make: ", self._make)
        print("Model: ", self._model)

    def getIdNumber(self):
        print("ID: ",self.__idnumber)

    def setIdNumber(self,idnumber):
        self.__idnumber = idnumber


#creating objects of the class
obj = Car()
obj._MakeAndModel()
obj.getIdNumber()
obj.setIdNumber("2334kdkd")
