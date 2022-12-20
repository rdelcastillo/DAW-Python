def menu(title, *options):
    while True:
        print(f"{title}")
        print("-" * len(title))
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        option = int(input("\nEscoja una opción: "))
        print()
        if 1 <= option <= len(options):
            return option
        print("Opción incorrecta.\n")