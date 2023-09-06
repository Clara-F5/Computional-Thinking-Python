numero = int(input("Digite um número: "))

verifica = numero % 3 == 0 and numero % 5 == 0

print("O número é divisível por 3 e 5 ao mesmo tempo?", verifica)
