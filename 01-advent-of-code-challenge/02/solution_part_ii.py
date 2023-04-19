#Atividade Dia 2
with open('Dia_02.in') as file:
    rodadas = [i for i in file.read().strip().split("\n")]

    part2resultados = {
        "A X": 3, "A Y": 4, "A Z": 8,
        "B X": 1, "B Y": 5, "B Z": 9,
        "C X": 2, "C Y": 6, "C Z": 7
    }

    pontuacaoPart2 = 0
    for rodada in rodadas:
        pontuacaoPart2 += part2resultados[rodada]

    print("A segunda resposta é: ", pontuacaoPart2)
