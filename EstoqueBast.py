while True:
    print('Hi! Welcome to my stock control. Lets get started!''\n')
    user_input3 = input('Quantos bastões tem em estoque: ')
    user_input = input('Quantas vendas teve de 30: ')
    user_input1 = input('Quantas vendas teve de 20: ')
    user_input2 = input('Quantas vendas teve de 10: ')
    question = input('Quer saber quantos bastões foram gastos? (s/n): ')
    user_inputint = int(user_input)
    user_inputint1 = int(user_input1)
    user_inputint2 = int(user_input2)
    user_inputint3 = int(user_input3)
    bast_30 = user_inputint * 30
    bast_20 = user_inputint1 * 20
    bast_10 = user_inputint2 * 10
    estoque_bast = user_inputint3 - (bast_10 + bast_20 + bast_30)
    if question.lower() in ["yes",'sim','y','s']:
            gastos = bast_10 + bast_20 + bast_30
            print('Seu estoque de bastão agora é:', estoque_bast, '\n''E hoje foram gastos:', gastos, 'bastões')
    elif question.lower() in ['no','n','não','nao']:
        print('Seu estoque de bastão agora é:', estoque_bast)
    else:
        print('I am sorry, I am a beginner in programming, in order to continue the program, please type either:''\n''(s/sim or n/nao)')
        continue
    again_question = input('Do you want to do it one more time? ')
    if again_question.lower() in ['no','n','não','nao']:
        print('Okay! Thanks for your time! Bye bye see you soon :)')
        break
    elif again_question.lower() in ['yes','y','sim','s']:
        continue
