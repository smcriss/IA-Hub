##

def bienvenida():
    print("Bienvenido al AI-hub")

bienvenida()
bienvenida()

def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Banana")
saludar("Cris")
saludar("Juanito perez")

def present(name, age):
    print(f"Hola {name}, tienes {age} años")

present("Cris", 19)
present("Pedrito", 12)

def restar(a, b):
    return a - b
resultado = restar(10, 4)
print(resultado)

age = int(input("Indique su edad: "))

def verificar_edad(age):
    if age >=18:
        return("Usted es mayor de edad")
    else:
        return("Usted es menor de edad")
resultado = verificar_edad(age)
print(resultado)


def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Error")
