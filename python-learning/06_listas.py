##

frutas = ["naranja", "manzana", "frutilla"]

frutas.sort()

for i in range(len(frutas)):
    print(f"{i + 1} - {frutas[i]}")

fruta = input("Que fruta buscas? ").lower()
if fruta in frutas:
    print("La fruta está en la lista")
    print(f"Está en la posición {frutas.index(fruta) + 1}")
else:
    print("La fruta no está en la lista")

##

listvariable = [2, 5, 9, 3, 1, 7]

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

listwrited = []

for i in my_list:
    if i in listwrited:
        continue
    else:
        listwrited.append(i)

my_list = listwrited
print("La lista con elementos únicos:")
print(my_list)
