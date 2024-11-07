limite = 0

while limite != 3:
    login = input("Digite seu login: ")
    senha = int(input("Digite sua senha: "))
    if login == "tds04" and senha == 123:
        print("Acesso Liberado")
    else:
        print("Acesso negado")
        limite += 1
print("Senha bloqueada!")
