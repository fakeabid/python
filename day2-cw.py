# You work for a bookstore that generates receipts for customers. Your task is to prepare a simple receipt using string techniques.
# Here’s what you need to do:
# Create a multiline string to store the receipt header.
# The customer bought 2 items:
# Book Title: "Python Basics" – ₹450
# Book Title: "Data Science Intro" – ₹600
# For each line showing the book and price, use a single string with basic {} placeholders and call format() once to fill in the values.
# Calculate the total price and add it similarly.
# Concatenate a thank-you message at the end.
# Make sure the output uses newline (\n) and tab (\t) for readability.
# Display the entire receipt in uppercase.

title1 = 'Python Basics'
price1 = 450

title2 = 'Data Science Intro'
price2 = 600

total = price1 + price2

receipt = f'''
    Book Title:\t"{title1}" - ₹{price1}\n
    Book Title:\t"{title2}" - ₹{price2}\n
    Total:\t{total}\n
'''

receipt += 'Thank you'

print(receipt.upper())