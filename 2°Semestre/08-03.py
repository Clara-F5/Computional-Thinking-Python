import os
from pprint import pprint
from json import dump, load


BD: list[dict] = []


def load_bd():
    file = "bd.json"
    if os.path.exists(file):
        with open(file) as f:
            return load(f)
    return []


def create_user():
    print("\nCadastrando um novo usuário")
    return {
        "nome": input("Nome: "),
        "endereco": input("Endereço: "),
        "documento": input("Documento: "),
    }


def serializer():
    with open("bd.json", "w") as f:
        dump(BD, f, indent=2)


def imprime_users():
    pprint(BD)


def opcoes():
    print("\n\nSelecione:")
    print("1 - Cadastrar usuário")
    print("2 - Imprimir usuários")


BD = load_bd()
while True:
    opcoes()
    option = input("\nOpção: ")
    match option:
        case "1":
            user = create_user()
            BD.append(user)
            serializer()
            pprint(user)
        case "2":
            imprime_users()
        case _:
            print("Opção inválida")
