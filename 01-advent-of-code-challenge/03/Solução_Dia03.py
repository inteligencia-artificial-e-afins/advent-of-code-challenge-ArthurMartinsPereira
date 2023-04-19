#Atividade Dia 3
from string import ascii_letters

with open('Dia_03.in') as file:
    data = [i for i in file.read().strip().split("\n")]

    somatotal = 0
    for mochila in data:
        metade = len(mochila)//2
        esquerda = set(mochila[:metade])
        direita = set(mochila[metade:])

        for prioridade, char in enumerate(ascii_letters):
            if char in esquerda and char in direita:
                somatotal += prioridade + 1

        print("Resposta da parte 1: ", somatotal)

        t = 3
        somatotal2 = 0
        for i in range(0, len(data), 3):
            mochila = data[i:t]
            t += 3

            for prioridade, char in enumerate(ascii_letters):
                if char in mochila[0] and char in mochila[1] and char in mochila[2]:
                    somatotal2 += prioridade + 1

        print("Resposta da parte 2: ", somatotal2)