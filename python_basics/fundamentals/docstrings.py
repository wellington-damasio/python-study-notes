# A documentation string is a string literal that you put as the first lines in a code block.

# Unlike a regular comment, a docstring can be accessed at run-time using obj.__doc__

# -----------------------------------
#       One-line docstrings
# -----------------------------------
def quicksort():
""" sort the string list using quicksort algorithm """

# -----------------------------------
#       Multi-line docstrings
# -----------------------------------
def increase(salary, percentage, rating):
    """ increase salary base on rating and percentage
    rating 1 - 2: no increase
    rating 3 - 4: increase 5%
    rating 4 - 6: increase 10%
    """

