contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0

valor = int(input("Digite um numero(negativo para sair!): "))

while valor >= 0 :
    
    if valor > -1 and valor <=25:
        contador1 += 1
    elif valor >= 26 and valor <=50:
        contador2 += 1
    elif valor >= 51 and valor <=75:
        contador3 += 1
    elif valor >= 76 and valor <=100:
        contador4 += 1
    valor = int(input("Digite um numero(negativo para sair!): "))
    
print(f"Numeros com intervalor 1 [0 à 25]: {contador1}")
print(f"Numeros com intervalor 2 [26 à 50]: {contador2}")
print(f"Numeros com intervalor 3 [51 à 75]: {contador3}")
print(f"Numeros com intervalor 4 [76 à 100]:{contador4}")