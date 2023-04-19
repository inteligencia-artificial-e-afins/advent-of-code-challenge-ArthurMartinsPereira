#Atividade Dia 1

with open('Dia_01.in') as file:
    data = [i for i in file.read().strip().split("\n")]

    print(data)


maximo = 0
maximo2 = 0
maximo3 = 0
quantelf = 0
for item in data:
 if item == '':
     quantelf = 0
 else:
     num = int(item)
     quantelf += num

 if quantelf > maximo:
     maximo3 = maximo2
     maximo2 = maximo
     maximo = quantelf
 elif quantelf > maximo2:
     maximo3 = maximo2
     maximo2 = quantelf
 elif quantelf > maximo3:
     maximo3 = quantelf


print('A quantidade de calorias que os três elfos carregam é: ', maximo + maximo2 + maximo3)