import json
import os

caminho_pasta = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(caminho_pasta, "data.json")

def EditarValor(chave, novo_valor):
    # Verifica se o arquivo existe
    if not os.path.isfile(caminho_arquivo):
        print("O arquivo data.json não existe.")
        return

    # Carrega os dados existentes do arquivo JSON
    with open(caminho_arquivo, "r") as arquivo:
        conteudo = json.load(arquivo)

    # Verifica se a chave está presente no dicionário
    if chave in conteudo:
        # Edita o valor da chave
        conteudo[chave] = novo_valor
        print("Valor editado com sucesso.")
    else:
        print("A chave não existe no dicionário.")

    # Escreve os dados atualizados de volta no arquivo JSON
    with open(caminho_arquivo, "w") as arquivo:
        json.dump(conteudo, arquivo)