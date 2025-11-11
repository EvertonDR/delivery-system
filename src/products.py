from os import system
from time import sleep


def products_menu(products_database):  # função que controla o menu dos produtos
    while True:
        system("cls")
        print(
            "PRODUTOS\n\n"
            "[1]Cadastrar\n"
            "[2]Mostrar todos\n"
            "[3]Buscar produtos\n"
            "[4]Atualizar produtos\n"
            "[5]Excluir produtos\n"
            "[6]Importar produtos\n"
            "[7]Início\n"
        )

        choice = input("Escolha uma opção: ")
        if choice == "1":
            create_product(products_database)
        elif choice == "2":
            show_products(products_database)
        elif choice == "3":
            get_product_by_id(products_database)
        elif choice == "4":
            update_product_by_id(products_database)
        elif choice == "5":
            delete_product_by_id(products_database)
        elif choice == "6":
            import_products(products_database)
        elif choice == "7":
            return products_database
        else:
            print("Escolha um número válido!")
            sleep(2)


def make_function_title_message(msg, size=52):
    system("cls")
    print("=" * size)
    print(msg.center(size))
    print("=" * size)


def create_product(database):
    make_function_title_message("CADASTRAR PRODUTOS")
    products = {}
    products["name"] = str(input("Nome do produto: ")).strip().title()
    products["price"] = float(input("Valor do produto: R$"))
    database.append(products.copy())
    input("\nProduto cadastrado! Pressione qualquer tecla para continuar.")


def show_products(database):
    make_function_title_message("LISTA DE PRODUTOS")
    if not database:
        print("Lista de produtos vazia!")
    else:
        print(f"{'No.':<5}{'Produto':<40}{'Valor'}")
        for index, item in enumerate(database):
            print(f"{index:<5}{item["name"]:.<40}R${item["price"]:.2f}")
    input("\nPressione qualquer tecla para voltar.")


def get_product_by_id(database):
    make_function_title_message("BUSCAR PRODUTOS")
    search = int(input("Digite o ID do produto: "))
    if search > len(database) - 1 or search < 0:
        input("\nProduto não encontrado! Pressione qualquer tecla para continuar.")
    else:
        print(f"{'No.':<5}{'Produto':<40}{'Valor'}")
        print(
            f"{search:<5}{database[search].get("name"):.<40}R${database[search].get("price"):.2f}"
        )
        input("\nPressione qualquer tecla para voltar.")


def update_product_by_id(database):
    make_function_title_message("ATUALIZAR PRODUTOS")
    search = int(input("Digite o ID do produto: "))
    if search > len(database) - 1 or search < 0:
        input("\nProduto não encontrado! Pressione qualquer tecla para continuar.")
    else:
        print(f"{'No.':<5}{'Produto':<40}{'Valor'}")
        print(
            f"{search:<5}{database[search].get("name"):.<40}R${database[search].get("price"):.2f}"
        )
        new_name = (
            str(input("\nDigite um novo nome(Deixe vazio caso não queira alterar): "))
            .strip()
            .title()
        )
        if new_name:
            database[search]["name"] = new_name
        new_price = str(
            input("Digite um novo preço(Deixe vazio caso não queira alterar): ")
        ).strip()
        if new_price:
            database[search]["price"] = float(new_price)
        input("\nProduto atualizado! Pressione qualquer tecla para voltar.")


def delete_product_by_id(database):
    make_function_title_message("EXCLUIR PRODUTOS")
    search = int(input("Digite o ID do produto a ser excluído: "))
    if search > len(database) - 1 or search < 0:
        input("\nProduto não encontrado! Pressione qualquer tecla para continuar.")
    else:
        print(f"{'No.':<5}{'Produto':<40}{'Valor'}")
        print(
            f"{search:<5}{database[search].get("name"):.<40}R${database[search].get("price"):.2f}"
        )
        while True:
            answer = (
                input(
                    f"\nTem certeza que deseja excluir {database[search].get("name")}?[S/N]"
                )
                .strip()
                .lower()[0]
            )
            if "n" in answer:
                input("\nOperação cancelada! Pressione qualquer tecla para continuar.")
                break
            if "s" in answer:
                del database[search]
                input("\nProduto excluído! Pressione qualquer tecla para continuar.")
                break


def import_products(database):
    make_function_title_message("IMPORTAR PRODUTOS")
    products = {}
    try:
        with open("./load_data/products.txt", "rt+") as file:
            print("Os seguintes produtos foram importados:\n")
            for line in file:
                data = line.split(";")
                data[1] = data[1].replace("\n", "")
                print(f"{data[0]}\tR${data[1]}")
                products["name"] = str(data[0]).strip().title()
                products["price"] = float(data[1])
                database.append(products.copy())
            input("\nPressione qualquer tecla para voltar.")
    except:
        print("Arquivo não encontrado!")
        input("\nPressione qualquer tecla para voltar.")
