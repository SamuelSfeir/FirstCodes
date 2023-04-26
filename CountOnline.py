# A program to check how many people are online at this moment

def online_count(x):
    input('please, paste your database to check how many people are online right now: ')
    count = 0
    for key, value in x.items():
        if value.lower() == 'online':
            count += 1
    if count == 1:
        return 'There is only 1 person online'
    elif count > 0 and count != 1:
        return 'There are '+str(count)+' people online'
    else:
        return 'Please, check if the database is structured this way: name: online or name: offline and try again'


