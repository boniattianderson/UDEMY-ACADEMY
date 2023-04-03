try:
    entrada_1 = input('Digite um valor') 
    entrada_1 = entrada_1.replace(' ','')
    entrada_1 = float(entrada_1)
    escolha_uma_operacao = input('+ - * / :')
    entrada_2 = input('Digite um outro Valor')
    entrada_2 = entrada_2.replace(' ','')
    entrada_2 = float(entrada_2)

    if escolha_uma_operacao == '+':
        resultado = entrada_1+entrada_2
        print(f'O Resultado da operação é {resultado}')
    elif escolha_uma_operacao == '-':
        resultado = entrada_1-entrada_2
        print(f'O Resultado da operação é {resultado}')
    elif escolha_uma_operacao == '*':
        resultado = entrada_1*entrada_2
        print(f'O Resultado da operação é {resultado}')
    elif escolha_uma_operacao == '/':
        resultado = entrada_1/entrada_2
        print(f'O Resultado da operação é {resultado}')
    else:
        print('Escolha uma operação para prosseguir:')
except:
    print('Digite apenas números:')