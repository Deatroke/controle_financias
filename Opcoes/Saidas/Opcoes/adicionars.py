from Crud.insert import Insert
import uuid

def OpSaid():
    Nome = input("Informe o nome da entrada: ")
    Valor = float(input("Informe o valor da entrada: "))

    data = {
        "id": str(uuid.uuid4()),
        "nome": Nome,
        "valor": Valor
    }

    Insert(data, "saidas")