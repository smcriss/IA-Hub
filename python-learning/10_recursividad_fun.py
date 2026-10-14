# Cisco Python Essentials 1 - Recursividad
# Una funcion se llama a si misma hasta alcanzar el caso base.


def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


# Ejemplo del curso: fun(25) = 25 + 28 + 3 = 56
print(fun(25))
