import os
from Opcoes.Saidas.Opcoes.adicionars import OpSaid

def OpSaidas():
    print(20 * "-")
    print("SAIDAS")
    print(20 * "-")
    print("Opções: \n"  
        "1 - Adicionar\n"
        "2 - Editar\n"
        "3 - Excluir\n"
        "4 - voltar")
    
    escolha = int(input("Escolha uma das opções acima: "))

    if escolha == 1:
        os.system("cls")
        OpSaid()