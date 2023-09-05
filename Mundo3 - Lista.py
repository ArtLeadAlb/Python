'''
#ex. 78
lista = []
maior = menor = 0
for i in range(0,5):
    n = int(input(f'Digite um número para posição [{i}]: '))
    lista.append(n)

max = max(lista)
min = min(lista)

print(f'Lista criada:\n{lista}\n')

print(f'Menor valor foi {min} nas posições: ', end='')
for posicao, valor in enumerate(lista):
    if valor == min:
        print(f'{posicao}...')

print(f'Maior valor foi {max} nnas posições: ', end='')
for posicao, valor in enumerate(lista):
    if valor == max:
        print(f'{posicao}...')


#ex. 79
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado ou não foi digitado um número.')
        continue
    sair = input('Deseja sair? [S] / [N]: ').upper()
    if sair == 'S':
        print('Saindo...')
        break
    elif sair == 'N':
        print('Continuando...')
        continue
    else:
        print('Opção inválida.')
        continue
print(f' Lista digidata foi:\n {sorted(lista)}')


#ex. 80
lista =[]
for i in range(0,5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'Adicionado na posicao {posicao} da lista.')
                break
            posicao += 1
print(f'Os valores digitados em ordem foram {lista}.')

#ex. 81
valores = []
while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    sair = str(input('Deseja sair? ')).upper()
    if sair == 'S':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print('O número 5 faz parte da lista.')
else:
    print('O número 5 não faz parte da lista.')

#ex.82
n = []
pares = []
impares = []
while True:
    n.append(int(input('Digite um número: ')))
    sair = str(input('Deseja sair? ')).upper()
    if sair == 'S':
        break
for valor in n:
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print(f'Lista completa:{n}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')

#ex. 83
expressao = str(input('Digite a expressão: '))
lista = []
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')
'''

#ex. 84
