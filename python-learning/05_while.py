##

number = int(input("Ingresa un número: "))
while number < 10:
    print("El número es menor que 10")
    number = int(input("Ingresa un número: "))

if number >= 10:
    print("El número es mayor o igual a 10")

contador = 1
while contador <=5:
    print(contador)
    contador = contador + 1

for i in range (1,6,2):
    print(i)

contador = 5
while contador > 0:
    print(contador)
    contador = contador - 1
if contador == 0:
    print("Despegue!")

contador = 1
while contador <= 10:
    print(contador)
    if contador == 7:
        break
    contador = contador + 1

contador = 1
while contador <= 10:
    print(contador)
    contador = contador + 1
    if contador == 5:
        break

for i in range (1, 11):
    if i % 2 == 0:
        continue
    print(i)

for i in range (1, 11):
    if i % 2 == 0:
        print(i)

contador = 0
for i in range(1, 11):
    if i % 2 == 0:
        contador = contador + 1
print(contador)

# Ejercicio: contar números pares e impares hasta introducir 0
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares.
        even_numbers += 1

    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

# Ejercicio: adivinar el número secreto
secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

nummer = int(input("Ingresalo aquí: "))

while nummer != secret_number:
    print("Ja! Estas atrapado en mi bucle!!")
    nummer = int(input("Prueba otra vez loser: "))

print("Bien hecho rana! sigue haciendo magia!")

blocks = int(input("Ingresa el número de bloques: "))

hoch = 0
layer = 1

while blocks >= layer:
    hoch += 1
    blocks -= layer
    layer += 1
    if blocks < layer:
        break
        
print("La altura de la pirámide:", hoch)
