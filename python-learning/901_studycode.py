## Zahlenanalysator

nummer = int(input("Please text your number: "))

nummer3 = 0
nummer5 = 0
nummer35 = 0
nummernichts = 0

for i in range(1, nummer + 1):
    if i % 3 == 0 and i % 5 == 0:
            nummer35 += 1
            print(f"Número {i} - divisible por 3 y 5")
    elif i % 3 == 0:
            nummer3 += 1
            print(f"Número {i} - divisible por 3")
    elif i % 5 == 0:
            nummer5 += 1
            print(f"Número {i} - divisible por 5")
    else:
            nummernichts += 1
            print(f"Número {i} - normal")

print(f"Cantidad de numeros divisibles por 3: {nummer3}")
print(f"Cantidad de numeros divisibles por 5: {nummer5}")
print(f"Cantidad de numeros divisibles por 3 y 5: {nummer35}")
print(f"Cantidad de numeros normales: {nummernichts}")