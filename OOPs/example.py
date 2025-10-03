
from abc import ABC,abstractmethod
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    #Getter method for private variable
    def get_salary(self):
        return self.__salary

    #Setter method for private variable
    def set_salary(self,new_salary):
        if new_salary > 0:
            self.__salary=new_salary
        else:
            print("Invalid salary!")
        
    #Abstraction method
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language=language

    def work(self):
        print(f"{self.name} is coding in {self.language}")

    def show_info(self):
        print(f"Developer:{self.name} , language:{self.language} , salary:{self.get_salary()}")

class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size

    def work(self):
        print(f"{self.name} is managing a team of {self.team_size} members")

    def show_info(self):
        print(f"Manager:{self.name},Team_size:{self.team_size},Salary:{self.get_salary()}") 

#Testing all the concepts
dev=Developer("Alice",5000,"python")
mgr=Manager("Bob",80000,5)

dev.work()
mgr.work()

dev.show_info()
mgr.show_info()

print("original salary of alice:",dev.get_salary())
dev.set_salary(5500)
print("Updated salary of alice:",dev.get_salary())