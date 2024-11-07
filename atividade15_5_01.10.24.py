'''Modifique o programa anterior para exibir qual deles é o menor número'''
contador = 1
while contador <= 3:
    v1 =int(input("Digite o primeiro numero: "))
    contador = contador + 1 
    v2 = int(input("Digite o segundo numero: "))
    contador = contador + 1 
    v3 = int(input("Digite o terceiro numero: "))
    contador = contador + 1 

    if v1 < v2 and v1 < v3:
        print("O primeiro numero informado é o menor!")
    elif v2 < v1 and v2 < v3:
        print("O segundo numero informado é o menor!")
    elif v3 < v2 and v3 < v1:
        print("O terceiro numero informado é o menor!")
