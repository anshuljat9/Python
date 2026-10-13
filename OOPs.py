# Class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# class is pascal case like bina space ke naam [Anshuljat] .

# Methods is a set of functions defined inside a class that can be called on objects of that class.

class Atm:
    # __init__ is a special method in Python classes. It is called a constructor and is automatically invoked when an object of the class is created. It is used to initialize the attributes of the class.
    #Constructor is a special method that is automatically called when an object of the class is created. It is used to initialize the attributes of the class.
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hello, how would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()  
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            exit()

    def create_pin(self):
        self.pin = input("Enter your new pin: ")
        print("Pin created successfully!")
        self.menu()

    def deposit(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            amount = float(input("Enter the amount to deposit: "))
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Incorrect pin.")
        self.menu()

    def withdraw(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect pin.")
        self.menu()

    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print(f"Your balance is {self.balance}.")
        else:
            print("Incorrect pin.")
        self.menu()

#a = Atm()
#a.menu()


# Magic methods are special methods in Python classes that have double underscores at the beginning and end of their names. They are also known as dunder methods. These methods allow you to define how objects of your class behave with built-in Python operations.
# the most commonly used magic methods are __init__, __str__, __repr__, __add__, __sub__, __mul__, __truediv__, __len__, __getitem__, __setitem__, and many more. These methods allow you to define how your objects behave with built-in Python operations.
"""
class Faction:
    def __init__(self, num , den):
        self.num = num
        self.den = den

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        other_num = self.num * other.den + self.den * other.num
        other_den = self.den * other.den

        return "{}/{}".format(other_num, other_den)

    def __sub__(self, other):
            other_num = self.num * other.den - self.den * other.num
            other_den = self.den * other.den
    
            return "{}/{}".format(other_num, other_den)

    def __mul__(self, other):
            other_num = self.num * other.num
            other_den = self.den * other.den
    
            return "{}/{}".format(other_num, other_den)

    def __truediv__(self, other):
            other_num = self.num * other.den
            other_den = self.den * other.num
    
            return "{}/{}".format(other_num, other_den)


f= Faction (5, 2)
f1= Faction (6, 3)
print(f)  # Output: 5/2
print(f1)  # Output: 6/3
print(f + f1)  # Output: 27/6
print(f - f1)  # Output: 3/6
print(f * f1)  # Output: 30/6
print(f / f1)  # Output: 15/12

"""


# Encapsulation is the process of hiding the internal details of an object and exposing only the necessary information to the outside world. It is achieved by using access modifiers like private, protected, and public. In Python, we can use a single underscore (_) to indicate that an attribute or method is intended for internal use only (protected), and a double underscore (__) to indicate that an attribute or method is private.

# In Python nothing is truly private . 