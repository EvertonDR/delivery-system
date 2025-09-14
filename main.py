from time import sleep
from os import system
from products import products_menu
from clients import clients_menu
from orders import orders_menu


def main():
    products_database = []
    clients_database = []
    orders_database = []

    while True:
        system("cls")
        print(
            "SISTEMA DE GERENCIAMENTO\n\n"
            "[1]Produtos\n"
            "[2]Clientes\n"
            "[3]Pedidos\n"
            "[4]Sair\n"
        )
        choice = input("Escolha uma opção: ")

        if choice == "1":
            products_database = products_menu(products_database)

        elif choice == "2":
            clients_menu()

        elif choice == "3":
            orders_menu()

        elif choice == "4":
            return 0
        else:
            print("Escolha um número válido!")
            sleep(2)


if __name__ == "__main__":
    main()
