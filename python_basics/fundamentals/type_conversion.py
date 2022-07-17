# To get an input from users, you can use the input() function
value = input('Enter a value: ')
print(value)

# The input() returns a string, not an integer (or float)
# If you have to get user input like numbers to perform mathematical operations with them, your 
#application will result in errors.

# To solve this, you need to convert the strings to numbers before performing calculations
# The int() function converts a value into an integer

price = input('Enter the price ($): ')
tax = input('Enter the tax rate (%): ')

net_price = "{:.2f}".format(int(price) * (int(tax) / 100))

print(f'The net price is ${net_price}')

# Obs: To round the numbers, I used a function similat to the toString() in JavaScript
# "{:.2f}".format(number_to_format)  will format you number to a maximum of 2 numbers after the
#decimal point

# ------------------------------------------
#     Other type conversion functions
# ------------------------------------------
# - float(str) - converts a string to a floating-point number
# - bool(val) - converts a value to a boolean value
# - str(val) - return the string representation of a value

# ------------------------------------------
#      Getting the type of a value
# ------------------------------------------
# To get the type of a value, you can use the type(value) function
print(type(100)) # int
print(type('Hello')) # str
print(type(9.2)) # float
print(type(20 < 10)) # boolean

