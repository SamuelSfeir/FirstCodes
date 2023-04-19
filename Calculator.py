print('Welcome to my calculator! Lets get started')
while True:
    try:
        user_input_first_number = int(input('What number? '))
        user_input_operation = input('What operation do you want to do? ')
        user_input_second_number = int(input('With what number? '))
        if user_input_operation == '+':
            print(user_input_first_number + user_input_second_number)
            continue
        elif user_input_operation == '/':
            print(user_input_first_number / user_input_second_number)
            continue
        elif user_input_operation == '*':
            print(user_input_first_number * user_input_second_number)
            continue
        elif user_input_operation == '-':
            print(user_input_first_number - user_input_second_number)
            continue
    except:
        print('Please, type a valid number or operator')

