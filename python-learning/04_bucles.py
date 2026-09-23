for i in range(0, 5):
    print(i)

for i in range(0, 21, 2):
    print(i)

nombres = ("Ana", "Pedrito", "Juanito")
for nombre in nombres:
    print(f"Hola, {nombre}, bienvenido al AI-Hub.")

nombres = ("Ana", "Pedrito", "Juanito")
for nombre in nombres:
    for i in range(3):
        print(nombre, "Repetición", i + 1)

contador = 2

while contador < 20:
    print(contador)
    contador = contador * 2


