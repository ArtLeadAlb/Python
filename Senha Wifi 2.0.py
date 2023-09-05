import subprocess

informacoes = subprocess.check_output(["netsh", "wlan", "show", "profiles"], encoding='cp860')
arquivo = open('Senhas do Wifi.txt','w')
for i in informacoes.split('\n'):
    if "Usuários: " in i:
        p = i.find(':')
        nome_wifi = i[p+2:]
        informacoes = subprocess.check_output(["netsh", "wlan", "show", "profile", nome_wifi, "key", "=", "clear"], encoding='cp858')
        arquivo.write(informacoes)

        for linha in informacoes.split('\n'):
            if "Conteúdo da Chave" in linha:
                # pegar a senha
                pos = linha.find(":")
                senha = linha[pos+2:]

                arquivo.write(f'Wifi: {nome_wifi}\nSenha: {senha}\n')

arquivo.close()
