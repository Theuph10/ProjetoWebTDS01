print("Seja bem vindo ao quiz premiado")
print("Cada pergunta vale vale 2 pontos, caso você acerte a pergunta bonus você recebera mais 3 pontos, caso erre perdera 2")
nome = input("Digite seu nome:")
perguntas = ''
resposta = ''
pontuacao = 0 

print("Primeira pergunta:")
print("Qual das alternativas apresenta os Presidentes do Brasil em ordem de sucessão?")
print("A) Dilma Rousseff, Lula, Jair Bolsonaro, Lula")
print("B)Dilma Rousseff, Lula, Jair Bolsonaro, Lula")
print("C)Lula, Dilma Rousseff, Jair Bolsonaro, Lula")
print("D)Dilma Rousseff, Michel Temer, Jair Bolsonaro, Lula")
resposta = input("")

if resposta == 'B':
    pontuacao = 2
    print(f"Sua Resposta esta correta sua pontuação é:",pontuacao)  
else:
    print(f"Resposta errada, sua pontuação é:",pontuacao)

print("Segunda Pergunta:")
print("Qual o valor do salario minimo em 2024?")
print("A)R$1512.00")
print("B)R$1850.00")
print("C)R$1412.00")
print("D)R$600.00")
resposta= input("")

if resposta == 'C' or resposta == 'c':
    pontuacao = pontuacao + 2
    print(f"Sua resposta esta correta sua pontuação é:", pontuacao)
else:
    print(f"resposta errada, sua pontuação é:", pontuacao)

print("Terceira Pergunta")
print("Quantas bolas de ouro Messi tem?")
print("A)5 Bolas de ouro")
print("B)4 Bolas de ouro")
print("C)7 Bolas de ouro")
print("D)8 bolas de ouro")
resposta = input ("")

if resposta == 'D' or resposta == 'd':
    pontuacao = pontuacao + 2
    print(f"Sua resposta esta correta sua pontuação é:", pontuacao)
else:
    print(f"resposta errada, sua pontuação é:", pontuacao)

print("Quarta Pergunta")
print("Quem é alma mais honesta do brasil?")
print("A)Cumpanheiro Maduro")
print("B)Flavio Dino")
print("C)Padre Kelmon")
print("D)Luiz Inacio Lula Da Silva")
resposta = input ("")

if resposta == 'D' or resposta == 'd':
    pontuacao = pontuacao + 2
    print(f"Sua resposta esta correta sua pontuação é:", pontuacao)
else:
    print(f"resposta errada, sua pontuação é:", pontuacao)


print("Pergunta Bonus!!!!!!!!!")
print("Quem foi a primeira presidenta do Brasil")
print("A)Maria Helena")
print("B)Dilma Rousseff ")
print("C)Marina Silva")
print("D)Simone Tebet")
resposta = input ("")

if resposta == 'B' or resposta == 'b':
    pontuacao = pontuacao + 3
    print(f"Sua resposta esta correta sua pontuação é:", pontuacao)
else: 
    pontuacao = pontuacao - 2
    print(f"resposta errada, sua pontuação é:", pontuacao)

if pontuacao >= 0 and pontuacao <=2: 
    print("Sem recompensa")
elif pontuacao >=3 and pontuacao <=5:
    print("Recompensa de Bronze")
elif pontuacao >=6 and pontuacao <=8:
    print("Recompensa de Prata")
elif pontuacao >=9 and pontuacao <=10:
    print("Recompensa de Ouro") 
else:
    print("Você é um mestre!")














