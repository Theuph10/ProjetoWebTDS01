login = ''
senha = ''

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

while not (login == "tds04" and senha == "123"):
    print("Acesso negado")
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

print("Acesso Liberado")