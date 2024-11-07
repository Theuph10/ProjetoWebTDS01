'''
Escrever um algoritmo que lê 5 valores, um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação.
'''
contador = 0
valorN = 0
while contador != 5:
    valor =int(input("Digite um valor: "))
    contador += 1
    if valor < 0:
        valorN = valorN + 1
print(f"A quantidade de valores negativos foi: {valorN}")