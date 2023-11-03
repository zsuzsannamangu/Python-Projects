
#parent class
class Car:
    make = "unknown"
    model = "unknown"
    id_number = ""
    powertype = ""

    #we give two methods to the Car class:
    def information(self):
        msg = "\nmake: {}\nmodel: {}\nid_number: {}\npowertype: {}".format(self.make,self.model,self.id_number,self.powertype)
        return msg

    def owner(self):
        owner_name = input("Enter your name: ")
        print("Hello {}, your {} {} car is cool.".format(owner_name,self.make,self.model))

#child class instance #1
class Full_hybrid(Car):
    color = "blue"
    fun = True

    def source(self):
        msg = "\nFull hybrid vehicles can run on the internal combustion engine alone, the electric motors alone, or a combination of both."\
              " They come in color {}.".format(self.color)
        return msg

#child class instance #2
class Mild_hybrid(Car):
    doors = 4
    carseats = True

    def source(self):
        msg = "\nMild hybrid vehicles cannot run solely on either its internal combustion engine or its electric motors."\
              " They have {} doors.".format(self.doors)
        return msg

    #we give this child class the owner function but modified
    def owner(self):
        owner_name = input("Enter your name: ")
        owner_phone = input("Enter your number: ")
        return ("Hello {}, your {} {} car is cool.".format(owner_name,self.make,self.model))

#child class instance #3
class Plugin_hybrid(Car):
    camera = True

    def source(self):
        msg = "\nThey offer the possibility of driving on full-electric power without the worry of finding a charging station as it still has an internal combustion engine as a backup."
        return msg

    #we give this child class the owner function but modified again
    def owner(self):
        owner_question = input("Do you like this car? ")
        if (owner_question == "yes"):
            return ("Great.")
        else:
            return("Sorry to hear that.")

#instantiate all the above class objects:
    
if __name__ == "__main__":
    fullhybrid = Full_hybrid()
    fullhybrid.make = "Toyota"
    fullhybrid.model = "Prius"
    fullhybrid.id_number = "1234KF"
    fullhybrid.powertype = "hybrid"
    fullhybrid.owner()
    print(fullhybrid.information())
    print(fullhybrid.source())

    mildhybrid = Mild_hybrid()
    mildhybrid.make = "Dodge"
    mildhybrid.model = "Ram"
    mildhybrid.id_number = "2829KB"
    mildhybrid.powertype = "hybrid"
    print(mildhybrid.owner())
    print(mildhybrid.information())
    print(mildhybrid.source())

    pluginhybrid = Plugin_hybrid()
    pluginhybrid.make = "BMW"
    pluginhybrid.model = "X5"
    pluginhybrid.id_number = "2191KB"
    pluginhybrid.powertype = "hybrid"
    print(pluginhybrid.owner())
    print(pluginhybrid.information())
    print(pluginhybrid.source())
    
    
    

    
