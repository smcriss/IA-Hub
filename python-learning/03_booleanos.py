age = int(input("¿Cuántos años tienes? "))

print(age >=18)
print(age < 18)
print(age == 19)
print(age !=19)

print(age >= 18 and age < 30)
print(age < 18 or age > 60)
print(not age == 19)

if age >= 18 and age < 30:
    print("Su edad está en el rango de 18 a 29 años.")
