import random

mylist = ['Rock','Paper','Scissors']
first_player=random.choice(mylist)
second_player=random.choice(mylist)

print(f'fisrt player got {first_player} and the second player got {second_player}')
if first_player == second_player:
    print('We got a tie')
elif first_player == 'Rock' and second_player == 'Paper':
    print('Second player wins!')
elif first_player == 'Rock' and second_player == 'Scissors':
    print('first player wins')
elif first_player == 'Scissors' and second_player == 'Rock':
    print('second player wins')
elif first_player == 'Scissors' and second_player == 'Paper':
    print('second player wins')
elif first_player == 'Paper' and second_player == 'Rock':
    print('first player wins')
elif first_player == 'Paper' and second_player == 'Scissors':
    print('second player wins')


