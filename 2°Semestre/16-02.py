def f():
    bd = []

    while True:
        user = {
            "nome": input("Digite seu nome de usuario: "),
            "cpf":  input("Digite seu cpf: "),
            "email":  input("Digite seu email: "),
            "rg":  input("Digite seu rg: "),
        }
        bd.append(user)

        print("\n Usuário adicionado com sucesso!")
        if input("\n Deseja adicionar mais usuários? [s/n]: ") == "n":
            break

    return bd

BD = f()

print("Usuários adicionados: ",BD)
