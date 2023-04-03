while True:
    try:
        nome = input('Qual seu nome!? ')
        
        comando = nome.replace(' ','')
        if comando == 'sair':
            print('Programa encerrado')
            break
        e_mail = input('Digite seu e-mail!')
        e_mail = e_mail.replace(' ','')
        senha = input('Digite Sua Senha! ')
        print('OK')
        print(f'{nome}')
        altura = input('Qual Sua Altura')
        altura = altura.replace(' ','')
        altura = float(altura)
        print(f'{altura}')
        peso = input('Qual seu Peso')
        peso = peso.replace(' ','')
        peso = float(peso)
        imc = peso / (altura ** 2)
        print(f'{imc}')
    except: 
        print('E preciso informar algum valor para continuar')
