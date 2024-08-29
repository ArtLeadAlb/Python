import math

print('\n*************** S E E D ***************\n')

def v_placa(espessura_placa, largura_placa, h=200):
    v_placa = h * espessura_placa * largura_placa
    return v_placa


#função de definir o volume do moderador mais o volume da placa
def v_moderador_mais_placa(n_placas, largura_placa, h=200):
    v_moderador = (12.59/n_placas)*largura_placa*h
    return v_moderador


v_placa15 = v_placa(0.18212612,7.219992862) 
#calculo do volume do moderador
v_moderador15 = v_moderador_mais_placa(7, 7.219992862) - v_placa15
#calculo da razão Vm / Vf
r15 = v_moderador15 / v_placa15
print('Arranjo 15x15:')
print(f'Volume da placa = {v_placa15:.8} cm³ \nVolume do moderador = {v_moderador15:.9} cm³')
print(f'Razão Vm / Vf = {r15:.6} \n \n')


v_placa16 = v_placa(0.199271215, 6.374956739)
v_moderador16 = v_moderador_mais_placa(9 , 6.374956739) - v_placa16
r16 = v_moderador16 / v_placa16
print('Arranjo 16x16:')
print(f'Volume da placa = {v_placa16:.8} cm³ \nVolume do moderador = {v_moderador16:.9} cm³')
print(f'Razão Vm / Vf = {r16:.6} \n \n')


v_placa17 = v_placa(0.176834736, 6.666739966)
v_moderador17 = v_moderador_mais_placa(9 , 6.666739966) - v_placa17
r17 = v_moderador17 / v_placa17
print('Arranjo 17x17:')
print(f'Volume da placa = {v_placa17:.8} cm³ \nVolume do moderador = {v_moderador17:.9} cm³')
print(f'Razão Vm / Vf = {r17:.6} \n \n')

v_placa18 = v_placa(0.162273122, 7.443020163)
v_moderador18 = v_moderador_mais_placa(9 , 7.443020163)- v_placa18
r18 = v_moderador18 / v_placa18
print('Arranjo 18x18:')
print(f'Volume da placa = {v_placa18:.8} cm³ \nVolume do moderador = {v_moderador18:.9} cm³')
print(f'Razão Vm / Vf = {r18:.6}  \n \n')

v_placa19 = v_placa(0.1678992, 7.747725706)
v_moderador19 = v_moderador_mais_placa(7 , 7.747725706)- v_placa19
r19 = v_moderador19 / v_placa19
print('Arranjo 19x19:')
print(f'Volume da placa = {v_placa19:.8} cm³ \nVolume do moderador = {v_moderador19:.9} cm³')
print(f'Razão Vm / Vf = {r19:.6}  \n')



print('\n********** B L A N K E T **********\n')

#função de defino o volume do moderador mais o volume do pino
def volume_moderador_mais_pino(n, h=200):
    volume = h*(21.42/n)**2
    return volume

def volume_pino(raio=0, h=200):
    volume_pino = (math.pi*raio**2)*h
    return volume_pino


volume_pino15 = volume_pino(0.582097157)
#calculo do volume do moderador
volume_moderador15 = volume_moderador_mais_pino(15) - volume_pino15
#calculo da razão Vm / Vf
razao15 = volume_moderador15 / volume_pino15
print('Arranjo 15x15:')
print(f'Volume do pino = {volume_pino15:.8} cm³ \nVolume do Moderador = {volume_moderador15:.8} cm³')
print(f'Razão Vm/Vf = {razao15:.6}\n \n')

volume_pino16 = volume_pino(0.509152463)
volume_moderador16 = volume_moderador_mais_pino(16) - volume_pino16
razao16 = volume_moderador16 / volume_pino16
print('Arranjo 16x16:')
print(f'Volume do pino = {volume_pino16:.8} cm³ \nVolume do Moderador = {volume_moderador16:.8} cm³')
print(f'Razão Vm/Vf = {razao16:.6}\n \n')


volume_pino17 = volume_pino(0.482645355)
volume_moderador17 = volume_moderador_mais_pino(17) - volume_pino17
razao17 = volume_moderador17 / volume_pino17
print('Arranjo 17x17:')
print(f'Volume do pino = {volume_pino17:.8} cm³ \nVolume do Moderador = {volume_moderador17:.8} cm³')
print(f'Razão Vm/Vf = {razao17:.6}\n \n')


volume_pino18 = volume_pino(0.477355328)
volume_moderador18 = volume_moderador_mais_pino(18) - volume_pino18
razao18 = volume_moderador18 / volume_pino18
print('Arranjo 18x18:')
print(f'Volume do pino = {volume_pino18:.8} cm³ \nVolume do Moderador = {volume_moderador18:.8} cm³')
print(f'Razão Vm/Vf = {razao18:.6}\n \n')



volume_pino19 = volume_pino(0.454549276)
volume_moderador19 = volume_moderador_mais_pino(19) - volume_pino19
razao19 = volume_moderador19 / volume_pino19
print('Arranjo 19x19:')
print(f'Volume do pino = {volume_pino19:.8} cm³ \nVolume do Moderador = {volume_moderador19:.8} cm³')
print(f'Razao Vm/Vf = {razao19:.6} \n \n')



print('\n************** F I M **************\n')
