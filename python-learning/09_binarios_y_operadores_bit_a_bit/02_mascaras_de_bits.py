# Práctica con máscaras de bits
# El bit 3 tiene peso 8: 01000

registro = 22       # 10110
the_mask = 8        # 01000


def binario(numero):
    """Representa el registro usando cinco bits."""
    return format(numero, "05b")


print("Registro inicial:", binario(registro), "=", registro)
print("Máscara:         ", binario(the_mask), "=", the_mask)
print()

# 1. Revisar el bit 3
if registro & the_mask:
    print("El bit 3 está encendido.")
else:
    print("El bit 3 está apagado.")

# 2. Encender el bit 3
registro_encendido = registro | the_mask
print("Encender:", binario(registro_encendido), "=", registro_encendido)

# 3. Apagar el bit 3
registro_apagado = registro_encendido & ~the_mask
print("Apagar:  ", binario(registro_apagado), "=", registro_apagado)

# 4. Invertir el bit 3
registro_invertido = registro ^ the_mask
print("Invertir:", binario(registro_invertido), "=", registro_invertido)
