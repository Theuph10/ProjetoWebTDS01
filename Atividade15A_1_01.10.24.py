'''
Desenvolva um programa solicite uma temperatura e a escala. Depois converta a temperatura de Celsius para Fahrenheit e vice-versa, até que o usuário decida parar.
'''
temp = int(input("Informe a temperatura: "))
escala = int(input(f"1)Para converter a temperatura de Fahrenheit para Celsius\n2)Para converter de Celsius para Fahrenheit\nDigite uma opção: "))

if escala >= 3:
    print("------ Opção invalida ------")
elif escala == 2:
    f = temp *1.8 + 32
    print(f"Temperatura {f}°F")
elif escala == 1:
    C = (temp - 32)/1.8
    print(f"Temperatura {C:.1f}%")
