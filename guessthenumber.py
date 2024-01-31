import random

def szamkitalalo():
    gondolt_szam = random.randint(1, 100)
    probalkozasok = 0

    print("Üdv a Számkitaláló játékban!")
    print("A szám a 1 és 100 között van. Próbáld meg kitalálni!")

    while True:
        probalkozasok += 1
        tipp = int(input("Add meg a tipped: "))

        if tipp < gondolt_szam:
            print("A gondolt szám nagyobb. Próbáld újra!")
        elif tipp > gondolt_szam:
            print("A gondolt szám kisebb. Próbáld újra!")
        else:
            print(f"Gratulálok! Kitaláltad a számot {probalkozasok} próbálkozásból!")
            break

szamkitalalo()