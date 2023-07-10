import json
import os

caminho_pasta = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(caminho_pasta, "data.json")

def Insert(data, tipo):
    # Verifica se o arquivo existe
    if not os.path.isfile(caminho_arquivo):
        print("O arquivo data.json não existe.")
        return

    # Carrega os dados existentes do arquivo JSON
    with open(caminho_arquivo, "r") as arquivo:
        conteudo = json.load(arquivo)

    # Obtém o próximo ID disponível
    if tipo in conteudo and isinstance(conteudo[tipo], list):
        ids = [item['id'] for item in conteudo[tipo]]
        novo_id = max(ids) + 1 if ids else 1
    else:
        novo_id = 1

    # Adiciona o novo item com o ID gerado
    novo_item = {
        "id": novo_id,
        "data": data
    }
    conteudo.setdefault(tipo, []).append(novo_item)

    # Escreve os dados atualizados de volta no arquivo JSON
    with open(caminho_arquivo, "w") as arquivo:
        json.dump(conteudo, arquivo)

    print("Valor adicionado com sucesso.")
