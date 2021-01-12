n = range(1)
k = range(50)
list = []

for n in k:
    numeros = int(input("Diz um numero: "))
    list.append(numeros)

print("O maior numero é", max(list))