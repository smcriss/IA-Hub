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


# Indicar al usuario que ingrese una palabra
user_word = input("Ein wort bitte: ")

# y asignarlo a la variable user_word.
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
