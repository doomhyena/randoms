import pickle
import os

TODO_FILE = "todo.pkl"

def save_todo_list(todo_list):
    with open(TODO_FILE, "wb") as file:
        pickle.dump(todo_list, file)

def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "rb") as file:
            return pickle.load(file)
    return []

def print_todo_list(todo_list):
    print("\nTeendők:")
    if not todo_list:
        print("Nincs teendő.")
    else:
        for i, todo in enumerate(todo_list, 1):
            print(f"{i}. {todo}")

def add_todo(todo_list):
    new_todo = input("Adj hozzá egy új teendőt: ")
    todo_list.append(new_todo)
    save_todo_list(todo_list)
    print(f"{new_todo} hozzáadva a teendőkhöz.")

def remove_todo(todo_list):
    print_todo_list(todo_list)
    try:
        index = int(input("Válassz egy teendőt a sorszámával: ")) - 1
        removed_todo = todo_list.pop(index)
        save_todo_list(todo_list)
        print(f"{removed_todo} eltávolítva a teendőkből.")
    except (ValueError, IndexError):
        print("Érvénytelen sorszám. Próbáld újra.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\nVálassz egy műveletet:")
        print("1. Listázd a teendőket")
        print("2. Adj hozzá új teendőt")
        print("3. Távolíts el egy teendőt")
        print("4. Kilépés")

        choice = input("Add meg a választott művelet sorszámát (1/2/3/4): ")

        if choice == '1':
            print_todo_list(todo_list)
        elif choice == '2':
            add_todo(todo_list)
        elif choice == '3':
            remove_todo(todo_list)
        elif choice == '4':
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás. Kérlek válassz 1-től 4-ig.")

if __name__ == "__main__":
    main()