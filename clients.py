from time import sleep
from os import system


def clients_menu():  # função que controla o menu dos clientes
    clients = {}

    while True:
        system("cls")
        print(
            "CLIENTES\n\n"
            "[1]Cadastrar\n"
            "[2]Mostrar todos\n"
            "[3]Buscar por ID\n"
            "[4]Atualizar ID\n"
            "[5]Excluir cliente\n"
            "[6]Importar cliente\n"
            "[7]Início\n"
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
            ...

        elif choice == "7":
            break
        else:
            print("Escolha um número válido!")
            sleep(2)
