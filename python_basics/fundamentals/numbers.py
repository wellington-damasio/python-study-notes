# Python supports integers, floats, and complex numbers

# ---------------------------------------
#     Integers and Math Operations
# ---------------------------------------
print(20 + 10)
print(20 / 10)
print(20 * 10)
print( 20 - 10)
print(20**10)
print(20 - 10 * 2) # 0
print( (20 - 10) * 2 ) # 20

# ---------------------------------------
#      Floats and Math Operations
# ---------------------------------------
print(0.5 + 0.2)
print(0.5 - 0.2)
print(0.6 / 0.3)
print(0.5 * 0.5)

# The division of integers always returns a float
print(12 / 3) # 4.0

# If you mix and integer and a float in any arithmetical operation, the result is a float
print(0.5 + 1.5) # 2.0

# Due to internal representation of floats, Python will try to represent the result as preciselty as
#possible. However, you may get the result you would not expect sometimes
print(0.1 + 0.2)

# ---------------------------------------
#        Underscores in numbers
# ---------------------------------------
# To make long numbers reabable, you can group digits using underscores, like this
count = 10_000_000
print(count)


