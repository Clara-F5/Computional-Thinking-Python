from json import dump
import requests
from pprint import pprint

# r = requests.get("https://pokeapi.co/api/v2/pokemon/")
# pprint(r.json())

# with open("pok.json", "w") as f:
#     dump(r.json(),f, indent=2)

def hash_cpf(cpf:int):
    return cpf % 97

def busca_poke(poke_id: int):
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_id}/",
                     )
    return r.json

def poke_human(poke):
    return poke["name"]

cpf = int(input("digite seu cpf:"))
poke_id = hash_cpf(cpf)
poke = busca_poke(poke_id)

print(F"o Pokemon correspondente ao cpf{(cpf)} é: {poke_human(poke)}")