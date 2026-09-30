##

person = {
    "name" : "Cris",
    "age" : 20,
    "country": "Chile",
    "job" : "Desempleado",
    "language" : "Spanish",
}

"""
print(person["name"])
print(person["age"])
print(person["country"])
"""

for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")

if "age" in person:
    print("La clave age existe")

if "city" in person:
    print("La clave city existe")
else:
    print("La clave city no existe")

if "job" in person:
    print(person["job"])
else:
    print("No hay información sobre el trabajo")

if "language" in person:
    print(f"Idioma: {person["language"]}")
else:
    print("Idioma no registrado")

if "country" in person:
    print(f"El país es: {person["country"]}")
else:
    print("País no registrado")

print(person.get("city", "Ciudad no encontrada"))