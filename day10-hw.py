# You are building a simple blueprint for different types of website users (like Admins and Guests). Each user must have a name and an account creation year.
# Create a general User class with a constructor that stores the user's name and account year.
# Mark User as an abstract class using a special decorator so no object can be created from it directly.
# Add a concrete method account_age() that returns how many years old the account is (assume current year is 2025).
# Add an abstract method get_role() that must be defined by every subclass.
# Create two subclasses: Admin and Guest. Each should define their own version of get_role() returning 'Admin' and 'Guest' respectively.
# Also, demonstrate the use of a magic method __str__() in each subclass to print a user-friendly message.
# Create objects for both subclasses and print their role, account age, and object message using print()
from abc import ABC, abstractmethod
from datetime import datetime

class User(ABC):
    def __init__(self, name, acc_year):
        self._name = name
        self._acc_year = acc_year

    def account_age(self):
        today = datetime.now()
        return today.year - self._acc_year
    
    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    def get_role(self):
        return 'admin'
    
    def __str__(self):
        return f'hello, i am {self._name}, the admin of the page.'

class Guest(User):
    def get_role(self):
        return 'guest'
    
    def __str__(self):
        return f'hello, i am {self._name}, a guest.'
    

user1 = Guest('abid', 2022)
user2 = Admin('eren', 2003)

print(f'role: {user1.get_role()}')
print(f'role: {user2.get_role()}')

print(f'years active: {user1.account_age()}')
print(f'years active: {user2.account_age()}')

print(user1)
print(user2)