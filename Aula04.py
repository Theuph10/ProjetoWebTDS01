'''
numero = 1
limite = int(input("Digite o numero limite você quer contar")) 
while numero <= limite :
    print (numero)
    numero += 1

# o simbolo de += serve para fazer uma soma com atribuição
#numero += 1 ==> numero = numero +1

 #Soma 1 na variavel número
'''
#lower tranformar para minusculo
#print(nome.lower()) 

#upper transforma para maisculo
#print(nome.upper()) 

#startswith (stringBuscada) faz uma busca no inicio da palavra
#print(nome.startswith('a')) #busca palavra com a letra 'a'

#endswith(stringBuscada) faz uma busca no final da palavra 
#print(nome.endswith('a'))


while True:
    nome = input("Digite seu nome: ")
    if nome.lower().startswith('a'):
        print("Nome: ",nome)
    else:
        print("Nome não aceito!")
