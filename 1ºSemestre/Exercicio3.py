letra = input("Digite uma letra: ")

verifica = (letra in 'aeiou') | (letra in 'AEIOU')

print("é vogal? : ", verifica)
