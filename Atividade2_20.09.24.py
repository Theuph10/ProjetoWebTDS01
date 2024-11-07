n = int(input("Digite um numero: "))
resultado = ''

if n % 10 == 0:
    # print(f"O numero {n} é divisivel por dez!")
    resultado = ' 10 '
if n % 5 == 0:
    # print(f"O numero {n} é divisivel por cinco")
    resultado = ' 5 '
if n % 2 == 0:
    #print(f"O numero {n} é divisivel por dois")
    resultado = ' 2 '
if (n % 2 != 0) and (n % 5 != 0) and (n % 10 !=0) :
    print(f"O numero {n} não é divisivel por 2,5,10")
else:
    print("o numero é divivel por:", resultado)