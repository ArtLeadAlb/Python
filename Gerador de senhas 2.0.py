import random
import string

pontos = '!@#$%&*()_+=-[]{}/?'
valores = string.ascii_letters + string.digits + pontos

print('=' * 24)
print(f'   PROGRAMA INICIADO')
print('=' * 24)

while True:
#Gera a senha    
    quantidade = int(input(' Quantos caracteres? '))
    senha = ''
    for i in range(quantidade):
        senha += random.choice(valores)

    print('-' * 90)
    salvar = input(' Menu de Opções:\n [0] -> Gerar a senha e apagar quando o programa for fechado.\n [1] -> Salvar em um arquivo.\n Escolha : ')
#Salva a senha em um documento .txt   
    if salvar == '1':
        print('-' * 90)
        arquivo_senha = open('Senha.txt','w')
        assunto = input(' Para o que é a senha? ')
        user = input(' Qual é o usuário? ')
        arquivo_senha.write(f'Assunto: {assunto}\nUsuário: {user}\nSenha gerada: {senha}')
        arquivo_senha.close()
        print('-' * 90)
        print(f' Senha salva em um arquivo "Senha.txt" no mesmo local que esse programa foi executado.')
        print('-' * 90)
        
#Não salva a senha, só mostra
    elif salvar == '0':
        print('-' * 90)
        print(f' Senha gerada: {senha}')
        print('-' * 90)
    else:
        print(' Opção Inválida.')
#Opção de saída
    sair = input(' Deseja sair? [S] / [N]: ').upper()
    if sair == 'S':
        break
    elif sair == 'N':
        continue
    else:
        print(' Opção Inválida.')
