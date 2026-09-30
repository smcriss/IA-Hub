name = input("¿Cómo te llamas? ")

print("Hola,", name)
print("Bienvenido a Python.")

age = int(input("¿Cuántos años tienes, " + name + "? "))
print(type(age))
print(f"Genial, {name}, tienes {age} años.")

print(age + 1)

if age == 18:
    print("Enhorabuena, acabas de cumplir la mayoría de edad.")
elif age > 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

variablea = float(input("Ingrese el primer número: "))
variableb = float(input("Ingrese el primer número: "))

print("Resultado de la suma: ", variablea + variableb)
print("Resultado de la resta: ", variablea - variableb)
print("Resultado de la multipicación: ", variablea * variableb)
print("Resultado de la división: ", variablea / variableb)

print("\n¡Eso es todo, amigos!")

# Ejercicio: cálculo del impuesto anual
income = float(input("Introduce el ingreso anual: "))

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + 0.32 * (income - 85528)

if tax <= 0:
    tax = 0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

# Ejercicio: comprobar un año del calendario Gregoriano
year = int(input("Introduce un año: "))

if year < 1582:
    print("No esta dentro del período del calendario Gregoriano")
else:
    if year % 4 != 0:
        print(f"{year} es un año comun.")
    elif year % 100 != 0:
        print(f"{year} es un año bisiesto.")
    elif year % 400 != 0:
        print(f"{year} es un año comun.")
    else:
        print(f"{year} es un año bisiesto.")
