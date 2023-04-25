# I did this python challenge that requested a program that return only the indexes that are capital letters.

# So, first I did this following one:

def capital_indexes(x):
    z = 0
    for i in x:
        z = z + 1
        if i.isupper():
            print(z-1)
            
# Then I did this one:

def capital_indexes(x):
    for i in x:
        z = 0
        if i in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            z = z + 1
            return i,z-1
        
# And finally I did this one, which in my opinion, is the best one:

def capital_indexes(x):
    for index,letter in enumerate(x):
        if letter.isupper():
            print(index)

            
    
