matriz = [['00', '01 ', '02'],['10','11 ','12'],['20','21 ','22']]

def vitoria(matriz):
    if matriz[0][0] == matriz[1][0] == matriz [2][0]:
        return 'Você ganhou!'
    elif matriz[0][1] == matriz[1][1] == matriz [2][1]:
        return 'Você ganhou!'
    elif matriz[0][2] == matriz[1][2] == matriz [2][2]:
        return 'Você ganhou!'
        
    elif matriz[0][0] == matriz[0][1] == matriz [0][2]:
        return 'Você ganhou!'
    elif matriz[1][0] == matriz[1][1] == matriz [1][2]:
        return 'Você ganhou!'
    elif matriz[2][0] == matriz[2][1] == matriz [2][2]:
        return 'Você ganhou!'

    elif matriz[0][0] == matriz[1][1] == matriz [2][2]:
        return 'Você ganhou!'           
    elif matriz[0][2] == matriz[1][1] == matriz[2][0]:
        return 'Você ganhou!'

while True:

    print(f'\n{matriz[0][0]}|{matriz[0][1]}|{matriz[0][2]}')
    print('--------')
    print(f'{matriz[1][0]}|{matriz[1][1]}|{matriz[1][2]}')
    print('--------')
    print(f'{matriz[2][0]}|{matriz[2][1]}|{matriz[2][2]}\n')


    p1_linha = int(input('Player 1 - Digite a linha que deseja (0, 1 ou 2): '))
    p1_coluna = int(input('Player 1 - Digite a coluna que deseja (0, 1 ou 2): '))
    matriz[p1_linha][p1_coluna] = ' X '

    if vitoria(matriz) == "Você ganhou!":
        print('Parabéns, Player 1! Você ganhou!')
        break

    print(f'\n{matriz[0][0]}|{matriz[0][1]}|{matriz[0][2]}')
    print('--------')
    print(f'{matriz[1][0]}|{matriz[1][1]}|{matriz[1][2]}')
    print('--------')
    print(f'{matriz[2][0]}|{matriz[2][1]}|{matriz[2][2]}\n')

    vitoria(matriz)

    p2_linha = int(input('Player 2 - Digite a linha que deseja (0, 1 ou 2): '))
    p2_coluna = int(input('Player 2 - Digite a coluna que deseja (0, 1 ou 2): '))
    matriz[p2_linha][p2_coluna] = ' O '

    if vitoria(matriz) == "Você ganhou!":
        print('Parabéns, Player 2! Você ganhou!')
        break
