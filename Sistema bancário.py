saldo = 0
limite = 500
extrato = ''
n_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input('''
Selecione uma opção:
[1] -> Deposito
[2] -> Saque
[3] -> Extrato
[0] -> Sair
Opção: ''')

    if opcao == '1':
        valor = float(input('Valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito no valor de R$ {valor}\n'
        else:
            print('Valor inválido. Operação não realizada.')

    elif opcao == '2':
        valor = float(input('Valor a ser sacado: '))

        if valor > saldo:
            print('Operação não realizada. Saldo insuficiente.')
        elif valor > limite:
            print('Operação não realizada. Valor de saque excedido')
        elif n_saques >= LIMITE_SAQUES:
            print('Operação não realizada. Número de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque no valor de R$ {valor:.2f}\n'
            n_saques += 1
        else:
            print('Operação não realizada. Valor inválido.')

    elif opcao == '3':
        print('='*32)
        print('EXTRATO:')
        if extrato:
            print(extrato)
        else:
            print('Nenhuma operação foi realizada.')
        print('=' * 32)

    elif opcao == '0':
        break

    else:
        print('Opção inválida. Selecione uma das opções do menu.')
