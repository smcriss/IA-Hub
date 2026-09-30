# Tablas y reglas: binarios y operadores bit a bit

> Sesión de estudio del 30 de septiembre de 2026.

## Pesos de los bits

Cada posición binaria representa una potencia de 2.

| Posición del bit | 4 | 3 | 2 | 1 | 0 |
|---|---:|---:|---:|---:|---:|
| Peso decimal | 16 | 8 | 4 | 2 | 1 |

Para pasar de binario a decimal, se suman los pesos de las posiciones que contienen un `1`.

| Decimal | Descomposición | Binario |
|---:|---|---:|
| 15 | 8 + 4 + 2 + 1 | `01111` |
| 22 | 16 + 4 + 2 | `10110` |

## Tabla de verdad

Los operadores bit a bit comparan cada pareja de bits por separado.

| A | B | `A & B` | `A \| B` | `A ^ B` |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

## Reglas

- **AND `&`:** produce `1` solamente cuando ambos bits son `1`.
- **OR `|`:** produce `1` cuando al menos uno de los bits es `1`.
- **XOR `^`:** produce `1` cuando los bits son diferentes.
- **NOT bit a bit `~`:** invierte los bits. En Python se cumple `~x = -x - 1`.

## Ejercicios resueltos

| Operación | Comparación binaria | Resultado |
|---|---|---:|
| `6 & 3` | `110 & 011 = 010` | 2 |
| `6 \| 3` | `110 \| 011 = 111` | 7 |
| `6 ^ 3` | `110 ^ 011 = 101` | 5 |
| `15 & 22` | `01111 & 10110 = 00110` | 6 |
| `12 & 10` | `1100 & 1010 = 1000` | 8 |
| `~7` | `-7 - 1` | -8 |
| `~15` | `-15 - 1` | -16 |

## Diferencia entre `not` y `~`

`not` es un operador lógico: transforma el valor en verdadero o falso y después lo niega.

| Expresión | Resultado |
|---|---|
| `not 0` | `True` |
| `not 1` | `False` |
| `not 7` | `False` |

`~` es un operador bit a bit y trabaja con la representación binaria de un número entero.

```python
print(not 0)  # True
print(not 7)  # False
print(~7)     # -8
```

## Máscaras de bits

Una máscara permite revisar o modificar un bit concreto. En la sesión usamos el **bit 3**, cuyo peso es **8**.

```python
the_mask = 8  # 01000
```

| Objetivo | Operación | Regla |
|---|---|---|
| Revisar | `registro & the_mask` | Si el resultado no es 0, el bit está encendido |
| Encender | `registro \| the_mask` | OR fuerza el bit seleccionado a 1 |
| Apagar | `registro & ~the_mask` | AND con la máscara invertida fuerza el bit a 0 |
| Invertir | `registro ^ the_mask` | XOR cambia 0 por 1 o 1 por 0 |

```python
if registro & the_mask:
    print("El bit está encendido")
else:
    print("El bit está apagado")
```

## Resumen

Los operadores lógicos trabajan con valores completos como `True` y `False`. Los operadores bit a bit trabajan posición por posición sobre la representación binaria de números enteros. Una máscara selecciona el bit que se quiere revisar o modificar.
