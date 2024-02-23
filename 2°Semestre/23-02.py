# arquivo = open("./exemplo.txt")

# todo o conteúdo do arquivo
# texto = arquivo.read();

# todo o conteúdo do arquivo, quebrando em linhas
# texto = arquivo.readlines();

# todo o conteúdo do arquivo, linha a linha
# for line in arquivo.readlines():
#     print(line)

# for line in arquivo:
#     print(line)



# # todo o processo em um bloco só
#
# with open("/.exemplo.txt") as file:
#     for line in file:
#         print(line)

# # escrevendo texto no arquivo
# with open("exemplo.txt", "r+") as f:
#     texto = f.read()
#     f.write("new line")

#
arquivo = open("./exemplo.txt")
texto = arquivo.read()

conta_letras = {}
for letra in texto:
    conta_letras[letra] = 1 + conta_letras.get(letra, 0)


conta_palavras = {}
for palavra in texto.split():
    conta_palavras[palavra] = 1 + conta_palavras.get(palavra, 0)


max_palavra = [None, 0]
for char, count in conta_palavras.items():
    if max_palavra[1] < count:
        max_palavra = [char, count]

max_char = [None, 0]
for char, count in conta_letras.items():
    if max_char[1] < count:
        max_char = [char, count]

with open("resultado.txt", "w") as f:
    f.write(f"palavra mais frequente: {max_palavra[0]}")
    f.write(f"\nquantidade de vezes: {max_palavra[1]}")
    f.write(f"\nletra mais frequente: {max_char[0]}")
    f.write(f"\nquantidade de vezes: {max_char[1]}")

