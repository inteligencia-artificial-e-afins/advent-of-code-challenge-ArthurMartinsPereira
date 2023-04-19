#Atividade Dia 2
with open('Dia_02.in') as file:
    rodadas = [i for i in file.read().strip().split("\n")]

    resultados ={
        "A X":4, "A Y":8, "A Z":3,
        "B X":1, "B Y":5, "B Z":9,
        "C X":7, "C Y":2, "C Z":6
    }

    pontuacao = 0
    for rodada in rodadas:
        pontuacao += resultados[rodada]

    print("A primeira resposta é: ", pontuacao)
