# The goal of this challenge was to create a program that returns a string that has dots between the letters without dots
# And the opposite as well (if the string does not have dots, it will return with dots)

# So I thougth about two ways of doing that. As the first way, we have:

def add_dots(string):
    return ".".join([letter for letter in string])
def remove_dots(string):
    return string.replace(".","")
  
# As for the second way of doing it, we have:
def add_dots(string):
    for letter in string[:-1]:
        print(letter, end=".")
    return (string[-1])
def remove_dots(string):
    return string.replace(".","")

# And if we combine them two together, we have:

def add_remove_dots(string):
    if string.count(".") == 0:
        return ".".join(string)
    else:
        return string.replace(".","")
