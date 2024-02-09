import string

for i in range(10):
    print(i)

alfabeto = string.ascii_lowercase
vogais = "aeiou"

consoantes = alfabeto
for vogal in vogais:
    consoantes = consoantes.replace(vogal, '')


print("Vogais: ",  vogais)
print("Consoantes:", consoantes)
