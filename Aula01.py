'''
Para comentar em várias linhas, usamos as aspas simples 3 vezes, tudo que estiver entre elas, vai ser ignorado pelo copilador 
'''
#Para comentar em uma linha, usamos o #
print('hello word') #para mostrar texto usamos aspas, com o comado print
print(2)
print(5.8)

input("Qual seu nome? ") 



#variavel do tipo inteiro -> integer(int)
quantidade = 12 

#Variavel do tipo logica -> boolean(bool)
#True --> Verdadeiro
#False --> Falso
temEstoque = True #variaveis do tipo logico (bool) sempre guarda, os valores True ou False

print("Tipo da variavel produto: ", type(quantidade))
print("TIpo da variavel temEstoque: ", type(temEstoque))

'''
Soma --> | + |
----------------------
Subtração | - |
----------------------
Multiplacação | * |
-----------------------
Divisão | / |
------------------------
Divisão truncada | // |
------------------------
pontencia | ** |
------------------------
Módulo | % |
------------------------

'''
n1 = int(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

soma = n1 + n2 
sub = n1 + n2
mult = n1 + n2
div = n1 / n2
divT = n1 // n2 
mod = n1 % n2
pot = n1 ** n2

print("soma: ",n1, "+",n2, "=", soma)
print(f"Substração: {n1} - {n2} = {sub}")
print(f"Multiplicação: {n1} x {n2} = {mult}")
print(f"Divisão: {n1} / {n2} = {div}")
print(f"Divisão Truncada: {n1} // {n2} = {divT}")
print(f"Modulo: {n1} % {n2} = {mod}")
print(f"potencia: {n1} ** {n2} = {pot} ")

#Operadores Logicos 
'''
Igual | == |
--------------------
Diferente | != |
--------------------
Maior Igual |>=|
--------------------
Menor Igual |<=|
--------------------
E                | and|
-----------------------
OU               | or |
-----------------------
NÃO              | not|


'''