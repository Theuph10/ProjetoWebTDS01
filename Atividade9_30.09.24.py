'''Crie um algoritmo que, dado um número informado pelo usuário, imprima a tabuada dele de 1 a 10, 
de maneira que sejam impressos somente as multiplicações cujo resultado seja um número par'
'''
n = int(input("Digite um numero: "))
contador  = 1

while contador <= 10:
    resultado = n * contador
    
    
    if resultado % 2 == 0:
        print(f"O numero {n} multiplicado por {contador} é: {resultado}")
    
    contador += 1 


