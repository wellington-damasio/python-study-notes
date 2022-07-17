# WHITESPACE AND INDENTATION
# Python don't use `;` to separate statements
# Python uses whitespace and indentation to construct the code
def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1

# Calling function main
main()

# Continuation of statements
# A long statement can span multiple lines by using the backslash (\)
if (a == True) and (b == False) and \
    (c == True):
        print('Continuation of statements')

# IDENTIFIERS
# Identifiers are names that identify variables, functions, modules, classes, and other objects in 
#Python

# The name of and identifier needs to be a letter or an underscore (_).
# Python identifiers are case-sensitive

# KEYWORDS
False    class    finaly    is    return[
None    continue    for    lambda    try
True    def    from    nonlocal    while
and    del    global    not    with
as    elif    if    or    yield
assert    else    import    pass
break    except    in    raise


# To see what keywords python has, use:
import keyword
print(keyword.kwlist)

# String literals 
# Python uses quotes ('), double quotes ("), triple quotes (''') and triple-double quotes (""") to 
# denote a string literal
