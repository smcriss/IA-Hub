## Sistema de entrenamiento

sportername = input("- Schreiben Sie ihre name ein: ")

alter = int(input("- Schreiben Sie ihr alter ein: "))

setsnummer = int(input("- Wie viele sets wollen Sie machen?: "))

setsminuten = int(input("- Wie viele minutes pro set wollen Sie machen?: "))

if alter < 16:
    print("Jugendtraining")
elif alter <= 17:
    print("Mittleres Training")
elif alter >= 18:
    print("Erwachsene Training")

print("Beginn des training")

for i in range(1, setsnummer + 1):
    print(f"Set nummer: {i}.")

gesamtzeit = setsminuten * setsnummer
print("¡Ende des Training!")

if gesamtzeit >= 30:
    print("Langes training absolviert!")
else:
    print("Kurz training absolviert")
    
print()
print(f"{sportername} hat {setsnummer} sets gemacht")
print(f"Gesamtzeit: {gesamtzeit} minuten.")
