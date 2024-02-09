num = int(input("Digite um número inteiro:"))

if num > 0:
    mensagem = "POSITIVO"
if num < 0:
    mensagem = "NEGATIVO"
elif num == 0:
    mensagem = "ZERO"

print(mensagem)
