n = range(1)
k = range(20)
list = []

for n in k:
    numeros = int(input("Diz um numero par positivo: "))
    list.append(numeros)

print("O maior numero é", max(list))