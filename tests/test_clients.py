import builtins
import sys
from unittest.mock import Mock, patch

# Adiciona o diretório src ao sys.path para importar corretamente
sys.path.append("src/")  # noqa

from src.clients import (
    create_imported_clients,
    create_new_clients,
    delete_client_by_id,
    get_client_by_id,
    list_clients,
    update_client_by_id,
)

user_test_name = "Test User"
user_test_email = "test@mail.com"
user_test_address = "123 Test Street, Test City, TS"
user_test_phone = "8399205556"

test_client = {
    "name": user_test_name,
    "address": user_test_address,
    "email": user_test_email,
    "phone": user_test_phone,
}


@patch.object(
    builtins,
    "input",
    side_effect=[user_test_name, user_test_address, user_test_email, user_test_phone],
)
def test_create_new_clients(_: Mock):
    """
    Testa a criação de um novo cliente via entrada simulada.
    Verifica se o retorno é um dicionário com os dados corretos.
    """
    client = create_new_clients()

    assert isinstance(client, dict)
    assert client["name"] == user_test_name
    assert client["email"] == user_test_email
    assert client == test_client


def test_create_imported_clients():
    """
    Testa a criação de cliente importado (apenas nome e email).
    Verifica se os campos address e phone ficam como None.
    """
    client = create_imported_clients(user_test_name, user_test_email)

    assert isinstance(client, dict)
    assert client["name"] == user_test_name
    assert client["email"] == user_test_email
    assert client == {
        "name": user_test_name,
        "address": None,
        "email": user_test_email,
        "phone": None,
    }


@patch.object(builtins, "input", return_value="s")
def test_list_clients(_):
    """
    Testa a listagem de clientes.
    Apenas garante que a função roda sem erros com um cliente na base.
    """
    clients_database = [test_client]
    list_clients(clients_database)


def test_get_client_by_id():
    """
    Testa a busca de cliente pelo índice.
    Verifica se retorna o cliente correto.
    """
    clients_database = [test_client]
    client = get_client_by_id(clients_database, 0, early_return=True)

    assert isinstance(client, dict)
    assert client["name"] == user_test_name
    assert client["email"] == user_test_email
    assert client == test_client


def test_update_client_by_id():
    """
    Testa a atualização dos dados de um cliente.
    Simula entradas para alterar todos os campos e verifica se foram atualizados.
    """
    clients_database = [test_client]

    updated_name = "Updated Name"
    updated_email = "new_mail@mail.com"
    updated_address = "456 New Street, New City, NC"
    updated_phone = "8399200000"

    with patch.object(
        builtins,
        "input",
        side_effect=[
            updated_name,
            updated_address,
            updated_email,
            updated_phone,
            "s",
        ],
    ):
        updated_clients_database = update_client_by_id(clients_database, 0)

    assert isinstance(updated_clients_database, list)
    assert updated_clients_database[0]["name"] == updated_name
    assert updated_clients_database[0]["email"] == updated_email
    assert updated_clients_database[0]["address"] == updated_address
    assert updated_clients_database[0]["phone"] == updated_phone


def test_delete_client_by_id():
    """
    Testa a remoção de um cliente pelo índice.
    Verifica se a lista final fica vazia.
    """
    clients_database = [test_client]
    delete_client_by_id(clients_database, 0)

    assert isinstance(clients_database, list)
    assert len(clients_database) == 0
