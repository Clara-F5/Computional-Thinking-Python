seq = input("Digite sua sequencia:")

for numero in seq:
    numero = int(numero)

    print(numero)

    if numero % 3 == 0 and numero % 5 == 0:
        print("divisivel por 3 e 5")

    elif numero % 3 == 0:
        print("divisivel por 3")

    elif numero % 5 == 0:
        print("divisivel por 5")
    else:
        print("não é divisivel nem por 3 nem por 5")
