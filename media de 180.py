n = range(1)
k = range(180)
list = []

for n in k:
    numeros = int(input("Diz um numero: "))
    list.append(numeros)

print("A média é", sum(list)/180)