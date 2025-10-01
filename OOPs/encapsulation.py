class BadBankAccount:
    def __init__(self,balance):
        self.balance=balance

# account = BadBankAccount(0.0)
# account.balance=-1
# print(account.balance)

class BankAccount:
    def __init__(self):
        self._balance=0.0

    @property
    def balance(self):
        return self._balance

    def deposite(self,amount):
        if amount <= 0:
            raise ValueError("Deposite amount must be positive.")
        self._balance +=amount

    def withdraw(self,amount):
        if amount <=0:
            raise ValueError("Withdrawn amount must be positive.")
        if amount >= self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

account = BankAccount()
print(account.balance)
account.deposite(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)



#(Getter and Setter methods are part of Encapsulation in OOP.)

#Using Getter/Setter methods (classic style)

from datetime import datetime

class User:
    def __init__(self,username,email,password):
        self.username=username
        self._email=email #_(single underscore) : protecting data attribute
        self.password=password

    #Getter method for email
    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    #Setter method for email
    def set_email(self,new_email):
        if "@" in new_email and "." in new_email: #Validation
            print(f"Email Updated at {datetime.now()}")
            self._email = new_email
        else:print("Invalid email format,update failed!")

user1 = User("dantheman","dan@gmail.com","123")
#Accessing email
print(user1.get_email())

#Updating email(valid case)
user1.set_email("bsi7t3b2@8gr.com")
print(user1.get_email())

#Updating email(invalid case)
user1.set_email("wrong_email")
print(user1.get_email())


#Using @property (Pythonic way)
class User:
    def __init__(self,username,email,password):
        self.username=username
        self._email=email #_(single underscore) : protecting data attribute
        self.password=password

    @property
    def email(self):
        print("Email Accessed!")
        return self._email

    @email.setter
    def email(self,new_email):
        if "@" in new_email:
            self._email=new_email

user1 = User("dantheman","dan@gmail.com","123")
user1.email="this is my email"
print(user1.email)
