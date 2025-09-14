from time import sleep
from os import system


def orders_menu():  # função que controla o menu dos pedidos
    orders = {}

    while True:
        system("cls")
        print(
            "PEDIDOS\n\n"
            "[1]Novo pedido\n"
            "[2]Mostrar todos\n"
            "[3]Buscar por ID\n"
            "[4]Atualizar ID\n"
            "[5]Excluir pedido\n"
            "[6]Início\n"
        )
        choice = input("Escolha uma opção: ")

        if choice == "1":
            ...

        elif choice == "2":
            ...

        elif choice == "3":
            ...

        elif choice == "4":
            ...

        elif choice == "5":
            ...

        elif choice == "6":
            break

        else:
            print("Escolha um número válido!")
            sleep(2)
