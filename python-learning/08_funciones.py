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




