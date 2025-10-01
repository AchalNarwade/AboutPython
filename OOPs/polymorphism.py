#polymorphism(poly=many;morph=forms)

#the word polymorphism is derived from greek, and means "having multiple forms"

class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):
    def __init__(self,brand,model,year,number_of_doors):
        super().__init__(brand,model,year)
        self.number_of_doors=number_of_doors

    def start(self):
        print("car is starting.")

    def stop(self):
        print("car is stoping.")

class Plane(Vehicle):
    def __init__(self,brand,model,year,number_of_doors):
        super().__init__(brand,model,year)
        self.number_of_doors=number_of_doors

    def start(self):
        print("plane is flying.")

    def stop(self):
        print("plane is landing.")

class Motorcycle(Vehicle):
    def __init__(self,brand,model,year):
        super().__init__(brand,model,year)
    #     self.brand=brand
    #     self.model=model
    #     self.year=year

    def start(self):
        print("motorcycle is starting")

    def stop(self):
        print("motorcycle is stopping")

#creating a list of vehicle to inspect
vehicles=[
    Car("ford","focus",2008,5),
    Motorcycle("Honda","scoopy",2018),
    Plane("Beoing","747",2015,4)
]

# #loops through list of vehicle and inspect them
# for vehicle in vehicles:
#     if isinstance(vehicle,Car):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type
#         (vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()
#     elif isinstance(vehicle,Motorcycle):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type
#         (vehicle).__name__})")
#         vehicle.start_bike()
#         vehicle.stop_bike()
#     else:
#         raise Exception("Object is not valid vehicle")


for vehicle in vehicles:
    if isinstance(vehicle,Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Object is not a valid vehicle")