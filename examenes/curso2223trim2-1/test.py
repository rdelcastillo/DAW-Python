from util.menu import Menu
from cash_register import CashRegister


cash = CashRegister()

def main():
    menu = Menu("Entrada", "Salida", "Borrado del último movimiento", "Impresión de la caja", "Terminar",
                title="Gestión de la Caja Registradora")
    while True:
        opc = menu.choose()
        match opc:
            case 1: deposit()
            case 2: withdraw()
            case 3: delete_last()
            case 4: print_cash_register()
            case _: break
    print("Hasta la próxima :-)")


def deposit():
    amount, concept = input_movement("entrada")
    cash.add(amount, concept) if amount >= 0 else print_error()


def withdraw():
    amount, concept = input_movement("salida")
    cash.add(-amount, concept) if amount >= 0 else print_error()


def delete_last():
    try:
        cash.delete_last()
    except ValueError:
        print("ERROR. No hay movimientos en la caja.\n")


def print_cash_register():
    print(cash)


def input_movement(prompt):
    amount = input_amount(prompt)
    if amount < 0:
        return amount, None
    concept = input("Concepto: ")
    print()
    return amount, concept


def input_amount(prompt):
    while True:
        try:
            amount = float(input(f"\nCantidad en euros para la {prompt} de caja: "))
            break
        except ValueError:
            print("El valor introducido no es numérico, introduzca una cantidad numérica.")
    return amount


def print_error():
    print("\nERROR. Cantidad negativa.\n")


if __name__ == '__main__':
    main()
