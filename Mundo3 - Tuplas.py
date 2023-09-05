#ex. 72
tupla = 'zero','um', 'dois', 'três', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove', 'dez'
n = int(input('Escolha um número entre 1 e 10. '))
print(tupla[n])

# ex. 73
times = 'Botafogo', 'Flamengo', 'Grêmio', 'São Paulo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Athletico-PR', 'Fortaleza', 'Cruzeiro', 'Internacional', 'Atético-MG', 'Cuiabá', 'Santos', 'Corinthians', 'Bahia', 'Goiás', 'Coritiba', 'Vasco', 'América-MG'
for i in range(0, 5):
    print(f'{i+1}ª posição: {times[i]}')
print(f'Os 4 últimos colocados: {times[-4:]}')

print(f'Ordem alfabética: {sorted(times)}')

print(f' Botafogo está na posição: {times.index("Botafogo")+1}ª posição')

#ex. 74
from random import randint
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(n)
print(f'Menor: {min(n)} \nMaior: {max(n)}')

#ex. 75
n = (int(input('Digite um número: ')), int(input('Digite outro número: ')),int(input('Digite mais número: ')),int(input('Digite o último número: ')))
print(f'Números digitados: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O número três está na posição {n.index(3)+1}ª.')
else:
    print('O valor 3 não foi digitado.')
    print('Os valores pares são ', end='')
for i in n:
    if i%2 == 0:
        print(f'{i} ', end='')


#ex.76
produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('-'*30)
print(f'{"Listagem de preços":^30}')
print('-'*30)
for posicao in range(0,len(produtos)):
    if posicao%2 ==0:
        print(f'{produtos[posicao]:.<20}',end='')
    else:
        print(f'R$  {produtos[posicao]:>5.2f}')
print('-'*30)

#ex. 77
palavras = ('APRENDER','PROGRAMAR','LINGUAGEM',
            'PYTHON', 'CURSO', 'GRÁTIS', 'ESTUDAR')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos: ',end='')
    for letra in palavra:
        if letra.lower() in 'aãáàeéêioóu':
            print(letra,end='')
