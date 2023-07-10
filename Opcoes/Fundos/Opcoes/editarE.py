from Crud.Editar import EditarValor

def OpEdit():
    chave = input("Informe o ID do item que deseja editar: ")
    Nome = input("Informe o novo nome: ")
    Valor = float(input("Informe o novo valor: "))

    data = {
        "nome": Nome,
        "valor": Valor
    }

    EditarValor(chave, data)
