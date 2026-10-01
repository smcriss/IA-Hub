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

