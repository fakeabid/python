# You are building a basic user account system. Every user has a name and a year they joined. Your task is to:
# Create a general User class that cannot be used directly to make objects, but stores name and joining year.
# Add a method to calculate how many years the user has been on the platform (assume current year is 2025).
# Add two types of users: Customer and Vendor, each showing their specific role when asked.
# Use a special print message for each user that shows their name, role, and how many years they’ve been using the platform.
from datetime import datetime
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    def calc_years(self):
        today = datetime.now()
        return today.year - self.joining_year
    
class Customer(User):
    def __init__(self, name, joining_year):
        super().__init__(name, joining_year)
        self.role = 'customer'

    def show_role(self):
        return self.role

class Vendor(User):
    def __init__(self, name, joining_year):
        super().__init__(name, joining_year)
        self.role = 'vendor'

    def show_role(self):
        return self.role
    
user1 = Customer('abid', 2022)
user2 = Vendor('eren', 2003)

print(f'name: {user1.name}\nrole: {user1.role}\nyears active: {user1.calc_years()}\n')
print(f'name: {user2.name}\nrole: {user2.role}\nyears active: {user2.calc_years()}\n')