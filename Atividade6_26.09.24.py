votos_total = 0
vencedor = 0
brancos = 0
nulos = 0
jair = 0
pablo = 0
ricardo = 0
porcentagem_branco = 0 
porcentagem_nulos = 0
option = ""
vencedor = ""

while option !="6":
    option = input(f"Escolha um candidato:\n1.Jair Messias Rodrigues \n2.Pablo Marçal \n3.Ricardo Salles \n4.Nulo \n5.Branco \nDigite o numero de seu candidato")
    if option ==  '1': 
        votos_total += 1
        jair += 1
    elif option == '2':
        votos_total += 1
        pablo +=1
    elif option == '3':
        votos_total += 1
        ricardo += 1
    elif option == '4':
        votos_total += 1
        nulos += 1
        if nulos >= 1:
            porcentagem_nulos = (nulos/votos_total)*100
    elif option == '5':
        votos_total +=1
        brancos +=1
        if brancos >= 1: 
            porcentagem_branco = (brancos/votos_total)*100
    if option != '1' or option != '2' or option != '3' or option != "4" or option != '5' or option != '6':
        print('Opção selecionada invalida!')

    if votos_total > 0 :
        if jair > pablo and jair > ricardo:
            vencedor = "jair"
        elif pablo > jair and pablo > ricardo:
            vencedor = "pablo"
        elif ricardo > jair and ricardo > pablo:
            vencedor = "ricardo"
        else:
            print("Empate sem vencedor claro") 
       

print (f"A quantidade de votos total na urna foi {votos_total},\no candidato Jair Messias Rodrigues recebeu: {jair},\nO candidato Pablo Marçal {pablo},\nO candidato Ricardo Salles:{ricardo}, \nPorcentagem de Votos Nulos:{porcentagem_nulos:.2f}%,\nPorcentagem de Votos Brancos: {porcentagem_branco:.2f}% \nO vencedor é {vencedor}",)



 




