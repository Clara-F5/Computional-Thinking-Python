peso = float(input("digite seu peso:"))
altura = float(input("digite sua altura (em metros):"))

imc = peso/altura ** 2

print("Seu imc é", imc)

if imc < 18.5:
    mensagem = "Abaixo do peso"
elif 18.5 <= imc <= 24.9:
    mensagem = "Peso Normal"
elif 25.0 <= imc <= 29.9:
    mensagem = "Sobrepeso"
elif 30.0 <= imc <= 34.9:
    mensagem = "Obesidade grau 1"
elif 35.0 <= imc <= 39.9:
    mensagem = "Obesidade grau 2"
else:
    mensagem = "Obesidade grau 3 (mórbida)"

print(mensagem)
