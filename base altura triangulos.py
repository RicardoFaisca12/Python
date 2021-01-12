n = range(1)
k = range(50)
list = []
list1 = []

for n in k:
    base = int(input("Diz a base: "))
    altura = int(input("Diz a altura: "))
    list.append(base)
    list1.append(altura)

print("A area dos 50 triangulos é", sum(list) + sum(list1)/2)