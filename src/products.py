from os import system
from time import sleep

products = {}


def products_menu(products_database):  # função que controla o menu dos produtos
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
            create_product()
            products_database.append(products.copy())
        elif choice == "2":
            show_products(products_database)
        elif choice == "3":
            search_product_byid(products_database)
        elif choice == "4":
            ...
            # update_productid()
        elif choice == "5":
            delete_product_byid(products_database)
        elif choice == "6":
            ...
            # import_product()
        elif choice == "7":
            return products_database
        else:
            print("Escolha um número válido!")
            sleep(2)


def create_product():
    system("cls")
    print("=" * 52)
    print(f"{"CADASTRAR PRODUTO":^52}")
    print("=" * 52)
    products["name"] = str(input("Nome do produto: ")).strip().title()
    products["price"] = float(input("Valor do produto: R$"))
    input("\nProduto cadastrado! Pressione qualquer tecla para continuar.")


def show_products(database):
    system("cls")
    print("=" * 52)
    print(f"{"LISTA DE PRODUTOS":^52}")
    print("=" * 52)
    if len(database) == 0:
        print("Lista de produtos vazia!")
    else:
        print(f"{'No.':<5}{'Produto':<40}{'Valor'}")
        for index, item in enumerate(database):
            print(f"{index:<5}{item["name"]:.<40}R${item["price"]:.2f}")
    input("\nPressione qualquer tecla para voltar.")


def search_product_byid(database):
    system("cls")
    print("=" * 52)
    print(f"{"BUSCAR PRODUTO":^52}")
    print("=" * 52)
    search = int(input("Digite o ID do produto: "))
    if search > len(database) - 1 or search < 0:
        input("\nProduto não encontrado! Pressione qualquer tecla para continuar.")
    else:
        print(f"{'No.':<5}{'Produto':<40}{'Valor'}")
        print(
            f"{search:<5}{database[search]["name"]:.<40}R${database[search]["price"]:.2f}"
        )
        input("\nPressione qualquer tecla para voltar.")


def update_productid(database): ...


def delete_product_byid(database):
    system("cls")
    print("=" * 52)
    print(f"{"EXCLUIR PRODUTO":^52}")
    print("=" * 52)
    search = int(input("Digite o ID do produto a ser excluído: "))
    if search > len(database) - 1 or search < 0:
        input("\nProduto não encontrado! Pressione qualquer tecla para continuar.")
    else:
        print(f"{'No.':<5}{'Produto':<40}{'Valor'}")
        print(
            f"{search:<5}{database[search]["name"]:.<40}R${database[search]["price"]:.2f}"
        )
        while True:
            resp = (
                input(
                    f"\nTem certeza que deseja excluir {database[search]["name"]}?[S/N]"
                )
                .strip()
                .lower()[0]
            )
            if "n" in resp:
                input("\nOperação cancelada! Pressione qualquer tecla para continuar.")
                break
            if "s" in resp:
                del database[search]
                input("\nProduto excluído! Pressione qualquer tecla para continuar.")
                break


def import_product(): ...
