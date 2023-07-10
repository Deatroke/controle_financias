import os
from Opcoes.Fundos.Opcoes.adicionare import OpAdic
from Opcoes.Fundos.Opcoes.editarE import OpEdit

def OpFundos():
    print(20 * "-")
    print("ENTRADAS")
    print(20 * "-")
    print("Opções: \n"  
        "1 - Adicionar\n"
        "2 - Editar\n"
        "3 - Excluir\n"
        "4 - voltar")
    
    escolha = int(input("Escolha uma das opções acima: "))

    if escolha == 1:
        os.system("cls")
        OpAdic()
    elif escolha == 2:
        os.system("cls")
        OpEdit()
    