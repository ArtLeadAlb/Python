"""Famoso jogo da forca (ou palavra secreta)"""

import os
while True:
        
    palavra = input('Digite a palavra para que o jogo comece: ').lower()
    dica = input('Digite uma dica: ')
    os.system('cls')
    print('')
    letras_acertadas = ''
    numero_tentativas = 0
    print(f'Dica: {dica}.\n')

    while True:

        chute = input('Digite uma letra: ').lower()
        numero_tentativas += 1

        if len(chute) > 1:
            print('Digite apenas uma letra, por favor.')
            continue

        if chute in palavra:
            letras_acertadas += chute

        palavra_formada = ''
        for letra_secreta in palavra:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'

        print(f'Palavra formada: {palavra_formada}.')

        if palavra_formada == palavra:
            print('Parabéns! Você acertou a palavra!')
            print(f'A palavra era {palavra}!')
            print(f'Tentativas: {numero_tentativas}.')
            break
        
    opcao = int(input('Deseja jogar novamente (1) ou sair (0)? '))
    if opcao == 1:
        continue
    elif opcao == 0:
        break
    else:
        print('Opção inválida! Saindo...')
        break
