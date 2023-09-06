valorInicial = float(input("Digite seu valor inicial: "))
taxaJuros = float(input("Digite sua taxa de juros anual: "))
tempo = int(input("Digite seu tempo de aplicacao em anos: "))

juro = valorInicial * taxaJuros * tempo

print("Os seus juros simples resultam em: ", juro)
