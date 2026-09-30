# Números binarios y operadores bit a bit
# Sesión del 30 de septiembre de 2026


def mostrar_binario(numero, ancho=5):
    """Muestra un entero positivo con ceros a la izquierda."""
    return format(numero, f"0{ancho}b")


# Conversión entre decimal y binario
numero_15 = 15
numero_22 = 22

print("15 en binario:", mostrar_binario(numero_15))
print("22 en binario:", mostrar_binario(numero_22))
print()

# Operadores AND, OR y XOR
a = 6
b = 3

print("6  =", mostrar_binario(a, 3))
print("3  =", mostrar_binario(b, 3))
print("6 & 3 =", a & b, "->", mostrar_binario(a & b, 3))
print("6 | 3 =", a | b, "->", mostrar_binario(a | b, 3))
print("6 ^ 3 =", a ^ b, "->", mostrar_binario(a ^ b, 3))
print()

# Otros ejercicios resueltos
print("15 & 22 =", 15 & 22, "->", mostrar_binario(15 & 22))
print("12 & 10 =", 12 & 10, "->", mostrar_binario(12 & 10, 4))
print()

# NOT bit a bit: ~x = -x - 1
print("~7  =", ~7)
print("~15 =", ~15)
print()

# Diferencia entre not y ~
print("not 0 =", not 0)
print("not 7 =", not 7)
print("~7    =", ~7)
