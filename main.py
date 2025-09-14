def cadastroAgenda():
    agenda = {}
    lista = []
    nomeCliente = str(input("Nome do cliente: "))
    divida = str(input("VALOR DA DIVIDA EM R$: "))
    telefone = str(input("TELEFONE DO CLIENTE: "))
    endereco = str(input("ENDEREÇO DO CLIENTE: "))
    lista.append(divida)
    lista.append(telefone)
    lista.append(endereco)
    agenda[nomeCliente] = lista[:]

    return agenda


def attValores(lista):
    nome = str(input("Qual o nome do cliente para atualização? "))
    for i in lista:
        for k in i.keys():
            if k == nome:
                i[nome][0] = str(input("Atualize o valor da divida: R$"))
                print("Valor da divida atualizado com sucesso!")


def removeClientes(lista):
    remove = []
    for i in lista:
        for k, v in i.items():
            if v[0] == "0":
                i[k] = "USUARIO SEM DIVIDAS"
                remove.append(k)

    for i in range(0, len(remove)):
        cont = 0
        remocao = remove[i]
        for d in lista:
            for k in d.keys():
                if k == remocao:
                    del lista[cont]
            cont += 1


def buscaNome(lista):
    cont1 = 0
    cont2 = 0
    nome = str(input("Qual o cliente que você deseja ver os dados? "))
    for i in lista:
        for k, v in i.items():
            if k == nome:
                print(30 * "-")
                print(
                    f"A divida de {k} é de: R${v[0]}\n"
                    f"O telefone de {k} é: {v[1]}\n"
                    f"E o endereço de {k} é: {v[2]}"
                )
                cont1 += 1
            else:
                cont2 += 1
    print(
        f"Total de clientes pesquisados: {cont2 + 1}\n"
        f"cliente(s) pesquisados com o nome que você pesquisou: {cont1}"
    )


def buscarTodos(lista):
    for i in lista:
        for k, v in i.items():
            print(30 * "-")
            print(
                f"Cliente {k}\n"
                f"A divida dele(a) é de: R${v[0]}\n"
                f"O telefone dele(a) é: {v[1]}\n"
                f"E o endereço dele(a) é: {v[2]}"
            )
            continuar = input("Enter para continuar")
    del continuar


def main():
    clientes = []
    continuarCadastro = "S"

    while True:
        print(
            "1 - Cadastro de clientes\n"
            "2 - Atualização de valores\n"
            "3 - Remover clientes com divida 0\n"
            "4 - Buscar por nome de cliente\n"
            "5 - Mostrar todos os clientes\n"
            "6 - SAIR"
        )
        escolha = int(input("Oque voce deseja? "))

        if escolha == 1:
            while continuarCadastro == "S":
                clientes.append(cadastroAgenda())
                continuarCadastro = str(
                    input("Deseja continuar cadastrando? [S / N]").upper()
                )
            continuarCadastro = "S"

        elif escolha == 2:
            attValores(clientes)

        elif escolha == 3:
            removeClientes(clientes)

        elif escolha == 4:
            buscaNome(clientes)

        elif escolha == 5:
            buscarTodos(clientes)

        elif escolha == 6:
            print("Programa finalizado!")
            break


main()
