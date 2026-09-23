##

person = {
    "name": "Cris",
    "age" : 20,
    "country": "Chile"
}

"""
print(person["name"])
print(person["age"])
print(person["country"])
"""
person["language"] = "Spanish"
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