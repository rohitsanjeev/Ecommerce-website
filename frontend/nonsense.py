# class bankaccount:
#     def __init__(self,balance):
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#     def show_balance(self):
#         return self.balance
# #object
# account = bankaccount(100)
# account.deposit(1000)
# print(account.show_balance())

# Create a parent class Vehicle with a method start_engine() that prints "Engine started!".

# Create a child class Car that inherits from Vehicle.

# Override the start_engine() method in Car to print "Car engine started!".

# Create an instance of Car and call start_engine().

class Vehicle:
    def start_engine(self):
        print("engine started!")
        
# Create a child class Car that inherits from Vehicle.

# Override the start_engine() method in Car to print "Car engine started!".
class Car(Vehicle):
    def start_engine(self):
        print("car engine started")

# Create an instance of Car and call start_engine().
car = Car()
car.start_engine()


# reached home today please complete oops tmrw!!!!!!!!
# -----> polymorphism ------<

#one function, different behaviour
#one functions behaves differently for differnet objects.

class Bird:
    def fly(self):
        print("birds can fly")
class Penguin:
    def fly(self):
        print("penguins cannot fly")
#crerate instance
bird = Bird()
penguin = Penguin()


bird.fly()
penguin.fly()








