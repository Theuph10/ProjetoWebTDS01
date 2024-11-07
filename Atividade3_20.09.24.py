valor = float (input("Qual o valor desejado?"))
prestacao = int(input("Informe a quantidade de parcelas: "))
valorParcela = float ( valor / prestacao)



if prestacao < 12:
    print("O emprestimo precisa pelo menos de doze parcelas")

elif prestacao >= 12 and prestacao < 24:
    print("O emprestimo aprovado, sem juros!")

elif prestacao >=24 and prestacao <36:
    print(f"O emprestimo aprovado, com acrecimo de 10% ", ((valor*10)/100) + valorParcela)

elif prestacao >=36:
    print(f"O emprestimo aprovado, com acrecimo de 15% ",((valor*15)/100) + valorParcela)