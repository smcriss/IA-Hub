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


# Mes real vs indice de una lista
# --------------------------------
# Para una persona, los meses se expresan como 1-12:
# enero = 1, febrero = 2, ..., diciembre = 12.
#
# Pero las listas de Python empiezan en el indice 0:
# indice 0 = enero, indice 1 = febrero, ..., indice 11 = diciembre.
#
# Por eso usamos month - 1 SOLO al momento de buscar dentro de la lista.
# La funcion sigue recibiendo meses normales (1-12), y ella misma traduce
# ese valor al indice que necesita internamente.
#
# Ejemplo:
# month = 2  -> febrero
# month - 1 = 1
# days[1] = 28
#
# La idea es que quien use la funcion pueda escribir:
# days_in_month(2024, 2)
# y entender naturalmente que 2 significa febrero.


def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Convertimos temporalmente el numero de mes (1-12)
    # al indice de la lista (0-11).
    res = days[month - 1]

    if month == 2 and is_year_leap(year):
        res = 29

    return res


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)

    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")


# Dia del año
# ----------
# Esta funcion reutiliza days_in_month() para sumar los dias
# de todos los meses anteriores y luego agrega el dia actual.
#
# Ejemplo:
# day_of_year(2024, 3, 10)
# enero = 31
# febrero = 29
# dia actual = 10
# total = 31 + 29 + 10 = 70

def day_of_year(year, month, day):
    days = 0

    for m in range(1, month):
        md = days_in_month(year, m)
        if md is None:
            return None
        days += md

    md = days_in_month(year, month)

    if md is None:
        return None

    if day >= 1 and day <= md:
        days += day
        return days
    else:
        return None


print(day_of_year(2000, 12, 31))


# Conversión del consumo de combustible
# -------------------------------------

def liters_100km_to_miles_gallon(liters):
    miles = 100000 / 1609.344
    gallons = liters / 3.785411784
    miles_per_gallon = miles / gallons
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    kilometer = miles * 1609.344 / 1000
    liters = 3.785411784 / kilometer * 100
    return liters

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
