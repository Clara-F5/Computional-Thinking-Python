# URL: https://www.google.com/search?q=fiap
#
# SCHEMA:  (protocolo)
#   HTTP[S]: HyperText Transfer Protocol
#           - usado pra transferência de textos formatados, por exemplo: HTML, XML, JSON, etc...
#           - S do HTTPS: secure (ou seguro)
#               - Os dados são transportados de modo criptografado para
#                 que se alguém interceptar a mensagem, o conteúdo seja
#                 "irrelevante" por estar "ilegível".
#   Também existem outros protocolos de rede, como o FTP: file transfer protocol,
#   que eh usado para transferências de arquivos
#
# DOMÍNIO: por exemplo google.com
#         - depende de um serviço chamado DNS: domain name service
#           (serviço de resolução de nomes de domínio)
#         - o domínio é traduzido para um IP (ou endereço) do servidor
#           pelo serviço de DNS
#         - Por exemplo, em nosso teste, o domínio www.google.com
#           foi traduzido para "142.250.219.132"
#
# ENDEREÇO DE IP: localização física da máquina (ou computador, ou servidor)
# PORT: (ou porta) -- em geral, é escondido das URLs
#               - exemplos bem comuns: 8080, 8000, 5001
#               - o banco de dados Postgresql usa por padrão a porta 5432
#
#
# PATH: é um caminho
#          É uma especificação do recurso a ser utilizado, por ex. "/search"
#
#
#
# Query String Parameters:
#           - Utilizamos o caractere "?" para marcar o início dos parâmetros
#           - Podemos ter 1 ou mais parâmetros,
#             mas no caso de parâmetros múltiplos, a separação á por "&"
#           - No exemplo da busca com o google, utilizávamos apenas "q=fiap"


# Intuitivamente, digitar "www.google.com/search?q=fiap" no navegador,
# pode ser entendido como uma função que busca resultados no banco de dados,
# como, por exemplo:


BD = ["fiap-paulista", "abc", "abacate", "o endereço da fiap é"]


def search(q):
    results = [record for record in BD if q in record]
    return results


from pprint import pprint

pprint(search(q="fiap"))

# %%
# Instalando a biblioteca requests:
# Digitar o seguinte comando em um terminal
# com acesso ao python
#       python -m pip install requests
# OU apenas
#       pip install requests

# importamos a lib requests
import requests

# lista os últimos eventos públicos do github
# r = requests.get("https://api.github.com/events")
r = requests.get("https://pokeapi.co/api/v2/pokemon/")

# para acessar o resultado da requisição em formato de texto
r.text

# utiliza a json.loads "por baixo dos panos"
# para traduzir a string de r.text para o Python
resultado = r.json()

# resultado é uma variável com dados convertidos
# para objetos e estruras de dados Python,
# ou seja, dicionários, listas, inteiros, strings, etc..
# logo, podemos processar os dados e trabalhar com eles
# como já sabemos em Python
type(resultado)

# %%
# Request Method: GET
# Status Code: 200 OK
