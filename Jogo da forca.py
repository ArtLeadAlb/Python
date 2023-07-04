"""Famoso jogo da forca (ou palavra secreta)"""

import os

palavra = input('Digite a palavra para que o jogo comece:').lower()
os.system('cls')
print('')
letras_acertadas = ''
numero_tentativas = 0

while True:
    chute = input('Digite uma letra: ')
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
        sair=input("Para sair digite 's' e pressione Enter:")
        if sair =='s':
            exit()
        else:
            palavra = input('Digite a palavra para que o jogo comece:').lower()
            os.system('cls')
            print('')
            letras_acertadas = ''
            numero_tentativas = 0
