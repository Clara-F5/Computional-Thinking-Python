#DICIONARIO
##dicionário Python é uma forma
##de coleção de dados em que se
##uma chave e um valor correspondente

#{chave : valor}

dicionario ={
    "a": None,
    "b": 1,
    1: "a",
    2: (1 , 2 , 3), #tupla
    3 : [3 , 2, 1 ] #lista
}

##print(dicionario) - dicionario inteiro

##print(dicionario[1]) - o valor correspondente a chave

##dicionario[1] = "jurubeba" - alterar o valor da chave

##dicionario.get(1, 0) = "pessego" - forma mais otimizada :  se a chave não existir, retorna zero



#Procurar quantidade de cada letra em um texto

from pprint import pprint

texto = "mangaba melancia"
frequencia = {}

for letra in texto:
    frequencia[letra] = 1 + frequencia.get(letra, 0)

pprint(frequencia) #impressão em ordem alfabética

##quantidade de cada palavra em um texto

frequencia_palavras = {}
for palavra in texto.split():
    frequencia_palavras[palavra] = 1 + frequencia_palavras.get(palavra, 0)

pprint(frequencia_palavras)
