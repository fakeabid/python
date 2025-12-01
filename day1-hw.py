# Homework Problem:
# A grocery store wants to calculate the final bill for a customer. The store has 3 products: rice, sugar, and oil. Each product has a fixed price per kilogram:
# Rice: ?45 per kg
# Sugar: ?40 per kg
# Oil: ?130 per kg
# Assume a customer bought:
# 3 kg of rice
# 2.5 kg of sugar
# 1.8 kg of oil
# Your task:
# Use variables to store the prices and quantities.
# Use appropriate data types.
# Calculate and print the total price for each item and the final total bill.
# Show the total bill as an integer and also as a string.
# Convert the float values where needed using explicit conversion.
# Use random number generation to add a random ?5–?10 delivery charge.
# Show the final bill amount including delivery charge.
import random

price_rice = 45.0
price_sugar = 40.0
price_oil = 130.0

qty_rice = 3.0
qty_sugar = 2.5
qty_oil = 1.8

print(f'Total (rice) : {price_rice*qty_rice}')
print(f'Total (sugar) : {price_sugar*qty_sugar}')
print(f'Total (oil) : {price_oil*qty_oil}')

total = price_rice*qty_rice + price_sugar*qty_sugar + price_oil*qty_oil

print(f'Total : {total}')
print(f'Total : {int(total)}')
print(f'Total : {str(total)}')

delivery_charge = random.randrange(5,10)
print(f'Delivery charge : {delivery_charge}')
print(f'Final Total: {total + delivery_charge}')