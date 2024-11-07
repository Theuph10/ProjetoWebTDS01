'''Peça ao usuário para inserir um número e um limite e mostre a tabuada de multiplicação desse número até o limite.'''
numero = int(input("Digite um numero: "))
limite = int(input("Digite um limite para parar: "))

contador = 1

while contador <= limite:
    resultado = numero * contador
    print(resultado)
    contador += 1 
