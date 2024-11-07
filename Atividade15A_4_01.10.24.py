'''
Escreva um programa que imprima um triângulo de números, onde cada linha tem um número a mais que a anterior, até um número n fornecido pelo usuário. Exemplo: Se digitar 5 precisa exibir
'''

n = int(input("Digite até onde o limite do triângulo: "))
contador = 1

while contador <= n:
    t = 1  # Inicia a contagem dos números na linha
    while t <= contador:  # Imprime os números até o contador atual
        print(t, end=" ")  # Imprime o número t na mesma linha
        t += 1  # Aumenta t para o próximo número
    print()  # Pula para a próxima linha
    contador += 1  # Aumenta o contador para a próxima linha