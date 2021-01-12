n = range(1)
k = range(7)
list = []

for n in k:
    numeros = int(input("Diz um numero positivo: "))
    list.append(numeros)

print("O maior numero é", max(list),"e o menor é", min(list))