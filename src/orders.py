from os import system
from time import sleep


def create_order():  # Função para criar um novo pedido
    new_order = input("Digite seu pedido: ")
    return {"descricao": new_order}


def orders_menu(orders_database):  # Função que controla o menu dos pedidos
    order_id = []
    next_id = 1

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
            order = create_order()
            order["id"] = next_id
            orders_database.append(order)
            order_id.append(next_id)
            next_id += 1
            print()

        elif choice == "2":
            print(orders_database)

        elif choice == "3":
            id_seach = int(input("Digite o ID do pedido que deseja buscar: "))
            encontrado = False
            for order in orders_database:
                if order["id"] == id_seach:
                    print(f"Pedido encontrado: {order}")
                    confirmacao = (
                        input("Esse é o pedido que você procura? (s/n) ")
                        .strip()
                        .lower()
                    )
                    if confirmacao == "s":
                        print("Detalhes do pedido:")
                        print(order)
                        encontrado = True
                        break
            if not encontrado:
                input("Pressione Enter para buscar outro pedido ou voltar ao menu.")

        elif choice == "4":
            old_id = int(input("Digite o ID do pedido que deseja atualizar: "))
            for order in orders_database:
                if order["id"] == old_id:
                    new_id = int(input("Digite o novo ID para este pedido: "))
                    if new_id in order_id:
                        print("ID já existe. Tente novamente.")
                        sleep(2)
                        break
                    order["id"] = new_id
                    print("ID do pedido atualizado com sucesso!")
                    sleep(2)
                    break
            else:
                print("Pedido não encontrado.")
                sleep(2)

        elif choice == "5":
            order_delete = int(input("Digite o ID do pedido que deseja excluir: "))
            for order_delete in orders_database:
                print(f"Esse é o pedido que você deseja excluir? {order_delete}")
                confirmacao = (
                    input("Confirma a exclusão deste pedido? (s/n) ").strip().lower()
                )
                if confirmacao == "s":
                    orders_database.remove(order_delete)
                    print("Pedido excluído com sucesso!")
                    sleep(2)
                    break
                else:
                    print("Exclusão cancelada.")
                    sleep(2)
        elif choice == "6":
            break

        else:
            print("Escolha um número válido!")
            sleep(2)
