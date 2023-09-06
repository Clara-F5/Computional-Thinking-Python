idade = int(input("Digite sua idade: "))
tempo = int(input("Digite seu tempo de contribuição: "))

aposenta = (idade >= 65) or (idade >= 60 and tempo >= 30)

print("Aposenta?", aposenta)
