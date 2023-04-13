while True:
    input_estoqueNAV = input('Qual seu estoque de navalha atual: ')
    input_laminas = input('E suas lâminas: ') #estoque de lâminas
    input_pedidos = input('Quantas navalhas + 5 lâm teve: ')
    if input_estoqueNAV == 'done' or input_laminas == 'done' or input_pedidos == 'done':
        break
    estoqueNAV = int(input_estoqueNAV)
    laminas = int(input_laminas) #estoque de lâminas
    pedido = int(input_pedidos)
    estoqueFlam = laminas - (pedido * 5)
    estoqueFnav = estoqueNAV - pedido
    print('Seu estoque de navalha atual é:',estoqueFnav,'\n''E seu estoque de lâmina atual é:',estoqueFlam)
