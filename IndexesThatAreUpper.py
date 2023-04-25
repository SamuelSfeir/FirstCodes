def capital_indexes(x):
    z = 0
    for i in x:
        z = z + 1
        if i.isupper():
            print(z-1)
