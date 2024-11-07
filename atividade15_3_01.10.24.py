'''Modifique o programa anterior para que o usuário determine qual o intervalo da contagem. '''
contador = 0 
x = int(input("Digite um numero até qual o programa deve execultar: "))

while contador <= x:
    contador = contador + 1
    
    if contador % 3 == 0:
        print(contador)
