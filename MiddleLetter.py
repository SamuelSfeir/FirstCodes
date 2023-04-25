# A program that returns only the middle letters of a string.

def mid(x):
    if len(x) % 2 == 0:
        return "It does not have a middle letter because this string is even"
    else:
        return x[len(x)//2]
