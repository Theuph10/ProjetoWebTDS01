nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
idade = int(idade)

emergencia = 'Dor intensa, dificuldade respiratória grave,perda de consciência'
grave = 'fraturas visíveis, sangramentos moderados'
Preferencial = 'febre alta persistente, dores leves'


print("1 - Dor intensa, dificuldade respiratória grave, perda de consciência (todas as idades).")

print("2 - Fraturas visíveis, sangramentos moderados (todas as idades).")

print("3 - Febre alta persistente, dores leves (todas as idades).")
classificacao = input("Digite a classificação do paciente (1, 2 ou 3): ")
 
# Verifica se a classificação está correta
if classificacao not in ["1", "2", "3"]:
    print("Classificação inválida. Por favor, insira 1, 2 ou 3.")
else:
    if (idade <= 12 or idade >= 65) and (classificacao == "1" or classificacao == "2"):
        prioridade = "Paciente com prioridade"
    elif 12 < idade < 65:
        prioridade = "Não tem prioridade"
    else: 
        prioridade = "Preferencial"
    # Resumo das informações do paciente
    print("\nResumo do Paciente:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Classificação: {classificacao}")
    print(prioridade)