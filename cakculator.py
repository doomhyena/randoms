def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

while True:
    print("Válassz műveletet:")
    print("1. Összeadás")
    print("2. Kivonás")
    print("3. Szorzás")
    print("4. Osztás")
    print("5. Kilépés")

    choice = input("Add meg a választott művelet sorszámát (1/2/3/4/5): ")

    if choice == '5':
        print("Kilépés...")
        break

    try:
        num1 = float(input("Add meg az első számot: "))
        num2 = float(input("Add meg a második számot: "))
    except ValueError:
        print("Érvénytelen bemenet. Kérlek számokat adj meg!")
        continue

    if choice == '1':
        print(f"Eredmény: {add(num1, num2)}")
    elif choice == '2':
        print(f"Eredmény: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Eredmény: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Eredmény: {divide(num1, num2)}")
    else:
        print("Érvénytelen választás. Kérlek válassz 1-től 5-ig.")