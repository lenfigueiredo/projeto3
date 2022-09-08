# Projeto 3
# Objetivo: Escreva um programa em Python que colete dados de notícias políticas na
# página do G1 e os salve em um arquivo no formato html.
# Coloque o código e o arquivo html no seu GitHub.
# Dica: Use os pacotes requests.


# Importar requests

import requests

# função para obter as informações da pagina

def page_reader(endereco: str) ->  requests.models.Response:
    pagina = requests.get(endereco)
    return pagina

# gravar pagina em um arquivo html

def grava_pagina_web(resposta: requests.models.Response) -> None:
    arquivo = open('politica.html', 'wb')
    for texto in resposta.iter_content():
        arquivo.write(texto)
    arquivo.close()

    
def main():
    endereco = 'https://g1.globo.com/politica/'
    politica = page_reader(endereco)
    grava_pagina_web(politica)
    print(f"A página {endereco} foi gravada com sucesso no arquivo 'politica.html'.")
    
if __name__ == "__main__":
    main()
