import builtins
from unittest.mock import Mock, patch

from clients import (
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
    client = create_new_clients()

    assert isinstance(client, dict)
    assert client["name"] == user_test_name
    assert client["email"] == user_test_email
    assert client == test_client


def test_create_imported_clients():
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
def test_list_clients():
    clients_database = [test_client]
    list_clients(clients_database)


def test_get_client_by_id():
    clients_database = [test_client]
    client = get_client_by_id(clients_database, 0, early_return=True)

    assert isinstance(client, dict)
    assert client["name"] == user_test_name
    assert client["email"] == user_test_email
    assert client == test_client


def test_update_client_by_id():
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
        updated_client = update_client_by_id(clients_database, 0)
    assert isinstance(updated_client, dict)
    assert updated_client["name"] == updated_name


def test_delete_client_by_id():
    clients_database = [test_client]
    updated_clients_database = delete_client_by_id(clients_database, 0)

    assert isinstance(updated_clients_database, list)
    assert len(updated_clients_database) == 0
