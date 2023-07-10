from Crud.insert import Insert
import uuid

def OpAdic():
    Nome = input("Informe o nome: ")
    Valor = float(input("Informe o valor: "))

    data = {
        "id": str(uuid.uuid4()),
        "nome": Nome,
        "valor": Valor
    }

    Insert(data, "entradas")

    
    # fundos.update({Nome : Valor})
    # print("|{0:^16}|{1:^10}|".format("Nome", "Valor"))
    # print(f"|{'-'*16}|{'-'*10}|")
    # print("|{0:<16}|{1:^10}|".format(Nome, Valor))