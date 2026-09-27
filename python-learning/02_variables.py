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