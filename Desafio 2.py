def menu():
    menu = '''
    Selecione uma opção:
    [1] -> Deposito
    [2] -> Saque
    [3] -> Extrato
    [4] -> Nova conta
    [5] -> Listar contas
    [6] -> Novo usuário
    [0] -> Sair
    Opção: '''
    return input(menu)


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito no valor de R$ {valor}\n'
    else:
        print('Valor inválido. Operação não realizada.')
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, n_saques, limite_saques):
    if valor > saldo:
        print('Operação não realizada. Saldo insuficiente.')
    elif valor > limite:
        print('Operação não realizada. Valor de saque excedido')
    elif n_saques >= limite_saques:
        print('Operação não realizada. Número de saques excedido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque no valor de R$ {valor:.2f}\n'
        n_saques += 1
    else:
        print('Operação não realizada. Valor inválido.')
    return saldo, extrato


def mostrar_extrato(saldo, /, *, extrato):
    print('=' * 32)
    print('EXTRATO:')
    if extrato:
        print(extrato)
    else:
        print('Nenhuma operação foi realizada.')
    print('=' * 32)


def novo_usuario(usuarios):
    cpf = input('Digite os números do CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta já existente.')
        return
    nome = input('Nome completo: ')
    data_nascimento = input('Data de nascimento no padrão dd/mm/aaa: ')
    endereco = input('Informe o endereço (logadouro, nº, bairro, cidade/Estado: ')
    usuario.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuário cadastrado com sucesso!')


def filtrar_usuario(cpf, usuarios):
    filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return filtrados[0] if filtrados else None


def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print('Usuário não encontrado. Operação encerrada.')


def listar_contas(contas):
    for conta in contas:
        linha = (f'Agência: {conta["agencia"]}\nC/C: {conta["numero_conta"]}\nTitular: {conta["usario"]["nome"]}')


def main():
    saldo = 0
    limite = 500
    extrato = ''
    n_saques = 0
    limite_saques = 3
    AGENCIA = '0001'
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input('Valor do depósito: '))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input('Valor a ser sacado: '))

            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, n_saques=n_saques,
                                   limite_saques=limite_saques, )

        elif opcao == '3':
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)


        elif opcao == '5':
            listar_contas(contas)

        elif opcao == '6':
            novo_usuario(usuarios)

        elif opcao == '0':
            break

        else:
            print('Opção inválida. Selecione uma das opções do menu.')


main()
