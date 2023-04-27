# A program to return True if both of the parameters are ints and False if not
# There are two ways to do that (at least that I could think at the moment)
# First one:

def only_ints(x, y):
    return isinstance(x, int) and not isinstance(x, bool) and isinstance(y, int) and not isinstance(y, bool)

# Second one:

def only_int(x,y):
    return type(x) == int and type(y) == int
