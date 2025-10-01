#Inheritance

#Inheritance is a fundamental concept in object-oriented programming 
# that involves creating new classes(subclasses or derived classes)
# based on existing classes(superclasses or base classes)

#base class(parent class)
class Vehicle:
    def __init__(self,brand,model, year):
        #common attribute for all vehicles
        self.brand=brand
        self.model=model
        self.year=year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")

#Derived class (child class) Car inherits Vehicle
class Car(Vehicle):
    def __init__(self,brand,model,year,number_of_doors,
    number_of_wheels):
    #Call the parent (Vehicle) constructor using super()
      super().__init__(brand,model,year)
      #car specific attributes
      self.number_of_doors=number_of_doors
      self.number_of_wheels=number_of_wheels

#Derived class (child class) Bike inherits Vehicle
class Bike(Vehicle):
    def __init__(self,brand,model,year,number_of_wheels):
        #call the parent (Vehicle) constructor using super()
        super().__init__(brand,model,year)
        #bike specific attributes
        self.number_of_wheels=number_of_wheels

#create car object
car=Car("Ford","Focus",2008,5,4)

#create bike object
bike=Bike("Honda","Scoopy",2018,2)

print("Car:",car.__dict__)
print("Bike:",bike.__dict__)
car.start()
bike.start()