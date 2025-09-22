# 🧪 Testes Unitários do Módulo de Clientes

Este documento apresenta a estrutura e exemplos dos testes unitários para o módulo `clients` do projeto.

## 📂 Estrutura típica de testes em projetos Python

Um projeto Python geralmente organiza os testes assim:

```
meu_projeto/
├── src/                # Código-fonte principal
│   ├── __init__.py
│   └── clients.py
├── tests/              # Pasta com testes
│   ├── __init__.py
│   └── test_clients.py # Testes do módulo clients
├── requirements.txt
└── pytest.ini          # Configuração opcional do pytest
```

**Boa prática:**
Manter os testes separados em uma pasta (`tests/`) e usar nomes como `test_<arquivo>.py`.

---

## 📝 Testes do módulo `clients`

Os testes cobrem o ciclo completo de operações CRUD (Create, Read, Update, Delete) para clientes, simulando entradas do usuário e verificando o comportamento das funções.

### 1. Criar Novo Cliente

```python
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
```

- Usa `patch` para simular entradas do usuário.
- Verifica se a função retorna um dicionário válido com os dados corretos.

### 2. Criar Cliente Importado

```python
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
```

- Cria um cliente apenas com nome e email.
- Verifica se os campos opcionais ficam como `None`.

### 3. Listar Clientes

```python
@patch.object(builtins, "input", return_value="s")
def test_list_clients(_):
    """
    Testa a listagem de clientes.
    Apenas garante que a função roda sem erros com um cliente na base.
    """
    clients_database = [test_client]
    list_clients(clients_database)
```

- Testa a listagem de clientes.
- Garante que a função roda sem erros (não faz assert).

### 4. Buscar Cliente por ID

```python
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
```

- Recupera cliente da lista pelo índice.
- Verifica se o retorno é o cliente esperado.

### 5. Atualizar Cliente por ID

```python
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
        updated_client = update_client_by_id(clients_database, 0)
    assert isinstance(updated_client, dict)
    assert updated_client["name"] == updated_name
    assert updated_client["address"] == updated_address
    assert updated_client["email"] == updated_email
    assert updated_client["phone"] == updated_phone
```

- Simula novas entradas para atualizar o cliente.
- Confere se os dados realmente mudaram.

### 6. Deletar Cliente por ID

```python
def test_delete_client_by_id():
    """
    Testa a remoção de um cliente pelo índice.
    Verifica se a lista final fica vazia.
    """
    clients_database = [test_client]
    updated_clients_database = delete_client_by_id(clients_database, 0)
    assert isinstance(updated_clients_database, list)
    assert len(updated_clients_database) == 0
```

- Remove cliente pelo índice.
- Verifica se a lista final fica vazia.

---

## 🤖 Por que usar e como usar Mocks nos testes?

Mocks são objetos simulados que imitam o comportamento de objetos reais. Eles são essenciais em testes unitários para:

- **Isolar o código testado:** Permitem testar funções sem depender de entradas externas, como teclado, banco de dados ou APIs.
- **Simular cenários:** Você pode definir o retorno de funções, simular exceções ou controlar o fluxo do teste.
- **Evitar efeitos colaterais:** Não altera dados reais nem exige interação do usuário.

No Python, o módulo `unittest.mock` fornece ferramentas para criar mocks facilmente. O mais usado é o `patch`, que substitui objetos temporariamente durante o teste.

### Exemplo prático com patch

```python
from unittest.mock import patch

@patch.object(builtins, "input", side_effect=["João", "Rua A", "joao@email.com", "99999999"])
def test_create_new_clients(mock_input):
    client = create_new_clients()
    assert client["name"] == "João"
```

Neste exemplo, o `input` é simulado para retornar valores pré-definidos, permitindo testar a função sem interação manual.

### Dicas de uso

- Use `side_effect` para simular múltiplas entradas.
- Use `return_value` para simular retorno fixo.
- Sempre limpe ou desfaça o patch ao final do teste (usando decorator ou contexto).

Mocks tornam os testes mais rápidos, confiáveis e fáceis de manter!

---

## ✅ Conclusão

- Os testes garantem que o CRUD de clientes funciona corretamente.
- Utilizam boas práticas com `pytest` e `unittest.mock.patch`.
- Servem como referência para quem está começando com testes unitários em Python.
- Testes automatizados ajudam a evitar bugs e facilitam a manutenção do código.

---
