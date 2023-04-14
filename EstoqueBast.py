while True:
    user_input3 = input('Quantos bastões tem em estoque: ')
    user_input = input('Quantas vendas teve de 30: ')
    user_input1 = input('Quantas vendas teve de 20: ')
    user_input2 = input('Quantas vendas teve de 10: ')
    question = input('Quer saber quantos bastões foram gastos? (s/n): ')
    if user_input == 'done':
        break
    user_inputint = int(user_input)
    user_inputint1 = int(user_input1)
    user_inputint2 = int(user_input2)
    user_inputint3 = int(user_input3)
    bast_30 = user_inputint * 30
    bast_20 = user_inputint1 * 20
    bast_10 = user_inputint2 * 10
    estoque_bast = user_inputint3 - (bast_10 + bast_20 + bast_30)
    if question == "Yes" or question == "yes" or question == 'Sim' or question == 'sim' or question == 'y' or question == 'Y' or question == 'S' or question == 's':
            gastos = bast_10 + bast_20 + bast_30
            print('Seu estoque de bastão agora é:', estoque_bast, '\n''E hoje foram gastos:', gastos, 'bastões')
            break
    elif question == 'n':
        print('Seu estoque de bastão agora é:', estoque_bast)
    else:
        print('I am sorry, I am a beginner in programming, in order to continue the program, please type either:''\n''(s or n)')
        continue
