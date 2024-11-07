numero = int(input("Digite um número: "))

# Inicializa variáveis para armazenar os resultados
div10 = False
div5 = False
div2 = False

# Verifica a divisibilidade
if numero % 10 == 0:
    div10 = True
if numero % 5 == 0:
    div5 = True
if numero % 2 == 0:
    div2 = True

# Exibe os resultados
resultados = []
if div10:
    resultados.append("10")
if div5:
    resultados.append("5")
if div2:
    resultados.append("2")

if resultados:
    print(f"{numero} é divisível por: {', '.join(resultados)}.")
else:
    print(f"{numero} não é divisível por 10, 5 ou 2.")