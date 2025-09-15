import json
from os import system
from time import sleep


# função que controla o menu dos clientes
def clients_menu(clients_database: list):
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
            user_response = input("Criando cliente, deseja continuar? [s/n]")
            if user_response.lower() == "n":
                continue
            clients_database.append(create_new_clients())
            print("Usuario criado com sucesso!")
            sleep(1)
            print("Voltando ao Menu...")
            sleep(1)

        elif choice == "2":
            list_clients(clients_database)
        elif choice == "3":
            client_id = input("Qual id do usuario você quer ver? ")
            if not client_id.isnumeric():
                print("Digite um id numerico")
            else:
                get_client_by_id(clients_database, int(client_id))
        elif choice == "4":
            client_id = input("Qual id do usuario você quer atualizar? ")
            if not client_id.isnumeric():
                print("Digite um id numerico")
            else:
                clients_database = update_client_by_id(clients_database, int(client_id))
        elif choice == "5":
            client_id = input("Qual id do usuario você quer excluir? ")
            if not client_id.isnumeric():
                print("Digite um id numerico")
            else:
                delete_client_by_id(clients_database, int(client_id))
        elif choice == "6":
            clients_database = import_client_by_json(clients_database)
        elif choice == "7":
            return clients_database
        else:
            print("Por favor, scolha um número válido!!!")
            sleep(2)


def create_new_clients():
    print("Criando novo cliente")
    name = input("Por favor, me diga seu Nome: ")
    address = input(
        "Por favor, me diga seu Endereço [formato: Rua, n°, cidade, estado]: "
    )
    email = input("Por favor, me diga seu Email: ")
    phone = input("Por favor, me diga seu Telefone: ")

    new_client = {"name": name, "address": address, "email": email, "phone": phone}
    return new_client


def create_imported_clients(name, email, address=None, phone=None):
    new_client = {"name": name, "address": address, "email": email, "phone": phone}
    return new_client


def list_clients(clients_database: list[dict]):
    print("Clients: ")
    user_response = "n"
    while user_response.lower() == "n":
        for idx, value in enumerate(clients_database):
            print(
                f"Cliente - id: {idx} | Nome: {value['name']} - Email: {value['email']}"
            )
        user_response = input("Voltar ao menu? [s/n]")


def get_client_by_id(
    clients_database: list[dict], client_id: int, early_return: bool = False
):
    if not clients_database or client_id + 1 > len(clients_database):
        print("Id não existente")
        tprint("cliente nao encontrado")
        return None

    user_response = "n"
    while user_response.lower() == "n":
        value = clients_database[client_id]
        print(
            f"Cliente - {client_id} | Nome: {value['name']} - Email: {value['email']}"
        )
        if early_return:
            return value
        user_response = input("Voltar ao menu? [s/n]")
    return value


def update_client_by_id(clients_database: list[dict], client_id: int):
    print("Atualizando cliente que foi passado!")
    print("Se você nao quer atualizar o campo, aperte [enter]")
    candidate = get_client_by_id(clients_database, client_id, early_return=True)
    if not candidate:
        tprint("cliente nao encontrado")
        return None

    name = input("Por favor, me diga seu Nome: ")
    address = input(
        "Por favor, me diga seu Endereço [formato: Rua, n°, cidade, estado]: "
    )
    email = input("Por favor, me diga seu Email: ")
    phone = input("Por favor, me diga seu Telefone: ")
    updated_client = {
        "name": name if name else candidate["name"],
        "address": address if address else candidate["address"],
        "email": email if email else candidate["email"],
        "phone": phone if phone else candidate["phone"],
    }
    clients_database.insert(client_id, updated_client)
    clients_database.pop(client_id + 1)
    print("Usuario atualizado!")
    tprint("voltando ao menu")
    return clients_database


def delete_client_by_id(clients_database: list[dict], client_id: int):
    if not clients_database or len(clients_database) < client_id + 1:
        tprint("cliente nao encontrado, voltando ao menu!")
        return None

    candidate = get_client_by_id(clients_database, client_id, early_return=True)
    if not candidate:
        tprint("cliente nao encontrado")
        return None
    clients_database.pop(client_id)
    tprint("cliente deletado com sucesso!")


def import_client_by_json(clients_database: list[dict]):
    with open("clients.json", "r") as file:
        data: list[dict] = json.load(file)

    imported: dict
    for imported in data:
        if (
            "name" in imported and "email" in imported
        ):  # Dados que são requeridos e não opcionais
            address = imported.get("address")  # opcional, se nao tiver ignora
            phone = imported.get("phone")  # opcional, se nao tiver ignora
            new_client = create_imported_clients(
                imported["name"], imported["email"], address, phone
            )
            clients_database.append(new_client)

    tprint("clientes exportados com sucessos!")
    return clients_database


def tprint(param: str, sleep_time=2):
    sleep(sleep_time)
    print(param)
    sleep(sleep_time)
