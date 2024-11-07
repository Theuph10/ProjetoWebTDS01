'''
Faça um programa que peça ao usuário quantos valores ele deseja somar, depois solicite a entrada desses números e em seguida exiba a soma e a média entre eles. 
'''
limite = int(input("Digite quantos numeros você deseja somar: ")) 
contador = 0 
valorTotal = 0


while contador < limite:
    vl1 = int (input(f"Digite um valor a ser somado: "))
    valorTotal += vl1
    contador += 1

media = valorTotal/limite
print(f"A somar de todos os valores é:{valorTotal}\nE a media é: {media} ")

#Quebra  a linha
#Atribuição 