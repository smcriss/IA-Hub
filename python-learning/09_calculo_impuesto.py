income = float(input("Introduce el ingreso anual: "))

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + 0.32 * (income - 85528)

if tax <= 0:
    tax = 0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
