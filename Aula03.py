'''
No python, quando temos condições para realizarmos ações, usamos o if-elf- else
#Condicionais || if-elif-else

No python, quando temos condições para realizarmos ações, usamos o if-elif-else
SE              | if |
SENAO SE        | elif |
SENAO           | else |
 
sintaxe :
if *condicao* :
    *acao*
elif *condicao* :
    *acao*
else :
    *acao*
 
***OBS: O Python é uma linguagem de IDENTAÇÃO OBRIGATÓRIA, onde é possível demarcar cada bloco com base no recuo da linha



'''

print("1 - Aluno")
print("2 - Funcionario")
print("3 - Visitantes")

tipoAcesso = input("Selecione uma opção: ")

if tipoAcesso == "1" or tipoAcesso == "2":
    print("Acesso Liberado")
elif tipoAcesso == "3":
    print("Faça um cadastro para entrar!")
else:
    print("Acesso Negado!")