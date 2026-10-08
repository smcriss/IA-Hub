print("\n===ConcenTrack===")
print("-Registrieren Sie Ihre Lernsitzung: ")

# time register variable
pythonzeit = 0
deutschzeit = 0
linuxzeit = 0
lernensitzungen = 0
gastwahl = 99

# Choosing menu
while gastwahl != 0:
    gastwahl = int(input("\n1. Python \n2. Deutsch \n3. Linux \n0. Sitzung beenden\n"))

    if gastwahl == 0: # if the guest wants to finish the registration of the sesions, they must type the number 0.
        break

# the guest choosed to register a study sesion of Python.
    elif gastwahl == 1:
        pythonzeiteingegeben = int(input("\nWie vielen minuten haben Sie Python studiert?:\n"))
        if pythonzeiteingegeben <= 0:
            print("\nBitte geben Sie einen gültigen Wer ein, der grösser als 0 ist.")
        else:
            pythonzeit += pythonzeiteingegeben
            print("\n\nPython Sitzung erfolgreich gespeichert, Registrieren Sie Ihre Sitzung Auf: ")
            lernensitzungen += 1

# the guest choosed to register a study sesion of German. 
    elif gastwahl == 2:
        deutschzeiteingegeben = int(input("\nWie vielen minuten haben Sie Deutsch studiert?:\n"))
        if deutschzeiteingegeben <= 0:
            print("\nBitte geben Sie einen gültigen Wer ein, der grösser als 0 ist.")
        else:
            deutschzeit += deutschzeiteingegeben
            print("\n\nDeutsch Sitzung erfolgreich gespeichert, Registrieren Sie Ihre Sitzung Auf: ")
            lernensitzungen += 1

# the guest choosed to register a study sesion of Linux.
    elif gastwahl == 3:
        linuxzeiteingegeben = int(input("\nWie viele minuten haben Sie Linux studiert?:\n"))
        if linuxzeiteingegeben <= 0:
            print("\nBitte geben Sie einen gültigen Wert ein, der grösser als 0 ist.")
        else:
            linuxzeit += linuxzeiteingegeben
            print("\n\nLinux Sitzung erfolgreich gespeichert, Registrieren Sie Ihre Nächste Sitzung: ")
            lernensitzungen += 1
    else: # the registration can only be effective if the guest enter a number of one of the subjects in the list
        print("\nBitte wählen Sie eine gültige Sitzung aus.")

hauptkategorie = 0

if pythonzeit > deutschzeit and pythonzeit > linuxzeit:
    hauptkategorie = pythonzeit
elif deutschzeit > pythonzeit and deutschzeit > linuxzeit:
        hauptkategorie = deutschzeit
elif linuxzeit > pythonzeit and linuxzeit > deutschzeit:
            hauptkategorie = linuxzeit

if hauptkategorie == pythonzeit:
    hauptkategorie = "Python"
elif hauptkategorie == deutschzeit:
    hauptkategorie = "Deutsch"
elif hauptkategorie == linuxzeit:
    hauptkategorie = "Linux"

zeitsieg = None
gesamtstudienzeit = pythonzeit + deutschzeit + linuxzeit
if gesamtstudienzeit >= 120:
    zeitsieg = True
else:
    zeitsieg = False


# total overview of the sesions
print("\n\n=== Aufzeichnung abgeschlossen ===\n")
print(f"Sie haben: {lernensitzungen} Sitzungen registriert.")
print(f"Gesamtzeit für das Erlernen von Python: {pythonzeit} min.")
print(f"Gesamtzeit für das Erlernen von Deutsch: {deutschzeit} min.")
print(f"Gesamtzeit für das Erlernen von Linux: {linuxzeit} min.")
print(f"Gesamtstudienzeit: {pythonzeit + deutschzeit + linuxzeit} min.")
print(f"Die Kategorie mit der längsten Lernzeit war: {hauptkategorie}")

if zeitsieg == True:
    print("Tagesziel erreicht!")
else:
    print(f"\nTagesziel nicht erreicht, verbleibende Minuten: {120 - gesamtstudienzeit}")






        


