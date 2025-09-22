from os import system
from time import sleep


def products_menu(products_database):  # função que controla o menu dos produtos
    products = {}  # noqa

    while True:
        system("cls")
        print(
            "PRODUTOS\n\n"
            "[1]Cadastrar\n"
            "[2]Mostrar todos\n"
            "[3]Buscar por ID\n"
            "[4]Atualizar ID\n"
            "[5]Excluir produto\n"
            "[6]Importar produto\n"
            "[7]Início\n"
        )
        choice = input("Escolha uma opção: ")

        if choice == "1":
            product = create_product()
            products_database.append(product)

        elif choice == "2":
            ...

        elif choice == "3":
            ...

        elif choice == "4":
            ...

        elif choice == "5":
            ...

        elif choice == "6":
            ...

        elif choice == "7":
            return products_database
        else:
            print("Escolha um número válido!")
            sleep(2)


def create_product():
    return {}
