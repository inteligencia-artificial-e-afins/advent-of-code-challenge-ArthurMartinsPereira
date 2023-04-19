#Atividade Dia 6
with open("Dia_06.in") as file:
    input = file.read()

    for i in range(4, len(input)):
        r = set(input[(i - 4):i])
        if len(r) == 4:
            print("A resposta da parte 1 é: ", i)
            break

    for i in range(14, len(input)):
        r = set(input[(i - 14):i])
        if len(r) == 14:
            print("A resposta da parte 2 é: ", i)
            break