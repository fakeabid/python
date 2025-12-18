# Create a program for a mini library system that asks the user to enter a book title and publication year.
# If the book title contains only alphabets and spaces, accept it. Otherwise, show an error.
# The publication year must be a 4-digit number starting with “19” or “20”. If not, display an error.
# Use appropriate error handling to catch any invalid inputs and ensure a message is printed at the end whether or not there was an error.
import re

while True:
    try:
        title = input('enter book title: ')
        if not re.match("^[a-zA-Z ]+$", title):
            raise ValueError('title must contain only alphabets and spaces.')
        
        publication_year = input('enter publication year: ')
        if not re.match("^(19|20)\d\d$", publication_year):
            raise ValueError('publication year must be a 4-digit number starting with “19” or “20”.')
        break
        
    except ValueError as e:
        print(e)
        print('please try again.\n')

    finally:
        print('this message is always printed')