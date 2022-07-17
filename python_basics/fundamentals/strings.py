# A string is a series of characters. In python, anything inside quotes is a string.

message = 'This is a string in Python'
print(message)

message = "This is algo a string in Python"
print(message)

message = 'I\'m getting good at this language... It\'s so easy...'
print(message)

# ---------------------------------------
#      Creating Multiline strings
# ---------------------------------------
help_message = '''
Usage: mysql command
    -h  hostname
    -d database name
    -u username
    -p password
'''

print(help_message)

# ---------------------------------------
#   Using Variables with the f-strings
# ---------------------------------------
name = 'John'
message = f'Hi {name}'

print(message)

name = 'Wellington'
lastName = 'Damasio'
age = 19
gender = 'male'

message = f'''
Name: {name};
LastName: {lastName};
Age: {age};
Gender: {gender};
'''

print(message)

# ---------------------------------------
#    Concatenating Strings in Python
# ---------------------------------------
# When you place the string literals next to each other, Python automatically concatenates tem into one
#string
 
greeting = 'Good' ' morning' ', sir'
print(greeting)

# To concatenate two string variables, use the + operator
greeting = 'Good Morning'
name = 'Wellington'

greeting = greeting + ', ' + name

print(greeting)

# ---------------------------------------
#      Accessing string elements
# ---------------------------------------
str = 'Python String'
print(str[0]) # P
print(str[2]) # t
print(str[-1]) # g
print(str[-4]) # r

# ---------------------------------------
#     Getting the length of a string
# ---------------------------------------
str = 'Wellington'
str_len = len(str)
print(str_len) # 10

# ---------------------------------------
#       Slicing strings in Python
# ---------------------------------------
print(str[0:5])
# The code above returns the substring that includes the character of index 0 to index 5. Index 0
# index 0 included and index 5 excluded (0 to 4 basically)

print(str[5:]) # If you omit the where to stop, it goes to the end of the string
print(str[:6]) # If you omit the start, it begins in the index 0 of the string

# ---------------------------------------
#     Python strings are immutable
# ---------------------------------------
# You cannot change the string
str = 'Python String'
# str[0] = 'J' # Error, You cannot change a string

# If you want to modify a string you'll need to create a new one
new_str = 'J' + str[1:]
print(new_str)


