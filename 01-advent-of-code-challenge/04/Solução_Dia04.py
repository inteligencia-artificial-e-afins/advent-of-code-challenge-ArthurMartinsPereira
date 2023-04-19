#Atividade Dia 4
with open('Dia_04.in') as file:
    data =[i for i in file.read().strip().split("\n")]

    pares = 0
    pares_2 = 0
    for entrada in data:
        primeiro, segundo = entrada.split(",")

        primeiro_c,primeiro_f = map(int, primeiro.split("-"))
        segundo_c, segundo_f = map(int, segundo.split("-"))

        if (primeiro_c <= segundo_c and primeiro_f >= segundo_f) or (segundo_c <= primeiro_c and segundo_f >= primeiro_f):
            pares += 1

        if set(range(primeiro_c, primeiro_f + 1)) & set(range(segundo_c, segundo_f + 1)):
            pares_2 += 1

        print("A primeira resposta é: ", pares)
        print("A segunda resposta é: ", pares_2)