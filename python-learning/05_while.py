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

   


    




