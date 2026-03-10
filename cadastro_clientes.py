import csv
import os

ARQUIVO = "clientes.csv"


# cria o arquivo se não existir
def inicializar_arquivo():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nome", "email", "telefone", "senha"])


def cadastrar_cliente():

    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    senha = input("Senha: ")

    with open(ARQUIVO, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([nome, email, telefone, senha])

    print("Cliente cadastrado com sucesso!")


def login():

    email = input("Email: ")
    senha = input("Senha: ")

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for linha in reader:
            if linha["email"] == email and linha["senha"] == senha:
                print("Login realizado com sucesso!")
                return True

    print("Email ou senha incorretos.")
    return False


def listar_clientes():

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        print("\nClientes cadastrados:\n")

        for linha in reader:
            print(
                f"Nome: {linha['nome']} | Email: {linha['email']} | Telefone: {linha['telefone']}"
            )


def menu():

    while True:

        print("\n--- Sistema de Clientes ---")
        print("1 - Cadastrar cliente")
        print("2 - Login")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":

            if login():

                while True:

                    print("\n--- Área logada ---")
                    print("1 - Listar clientes")
                    print("2 - Logout")

                    opcao2 = input("Escolha: ")

                    if opcao2 == "1":
                        listar_clientes()

                    elif opcao2 == "2":
                        print("Logout realizado.")
                        break

        elif opcao == "3":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")


inicializar_arquivo()
menu()