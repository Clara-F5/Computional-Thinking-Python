# Arquivos JSON: Java Script Object Notation

# Exemplo de dado que pode se tornar um JSON
# d = {
#     "endereco": "SP capital ...",
#     "casa_ou_apto": "casa",
#     "compras_anteriores": [
#         123,
#         234234,
#         56734,
#         ...,
#     ],
# }

from json import load, dump, loads, dumps
# Com o load, a gente precisa de um obejto que possa ler,
# pois o load se encarrega de ler para nós
with open("./poke.json") as f:
    poke = load(f)["results"]


# Com o dump, a gente precisa de um obejto que possa escrever,
# pois o dump se encarrega de escrever para nós
with open("./lista_pokes.json", "w") as f:
    dump(poke, f, indent=2)


d = {"a": 1, "b": 2, "c": 3}
# Com o dumpS, a gente precisa apenas de uma objeto
d_codificado = dumps(d)  # retorna no formato de string
# {"a": 1, "b": 2, "c": 3} -> '{"a": 1, "b": 2, "c": 3}'


# Com o loadS, a gente precisa apenas de uma string
d_decodificado = loads(d_codificado)  # retorna no formato de objeto
# '{"a": 1, "b": 2, "c": 3}' -> {"a": 1, "b": 2, "c": 3}


# # Abstração de como a lib JSON poderia ter implementado
# # Não é um código que usamos no dia a dia
# def dump(arquivo, obj):
#     with open(arquivo, "w") as f:
#         obj_codificado = dumps(obj)
#         f.write(obj_codificado)


# def load(arquivo):
#     with open(arquivo) as f:
#         obj_codificado = f.read()
#         return loads(obj_codificado)
