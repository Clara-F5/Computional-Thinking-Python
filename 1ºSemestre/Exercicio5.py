nota = float(input("Digite sua nota nessa matéria: "))

faltas = int(input("Digite a quantidade de faltas: "))

verifica = nota >= 7 and faltas < 15

print("Foi aprovado? ", verifica)
