import os
import platform

from Opcoes.Fundos.index import OpFundos
from Opcoes.Saidas.index import OpSaidas

sistema_operacional = platform.system()

while True:
    os.system("cls")

    print("Opções: \n"
            " \n"  
            "1 - Fundos\n"
            "2 - Saidas\n"
            "3 - Detalhes\n"
            " ")
    escolha = int(input("Escolha uma das opções acima: "))
# Entradas
    if escolha == 1:
        os.system("cls")
        OpFundos()
        os.system("cls")
# Saidas
    if escolha == 2:
        os.system("cls")
        OpSaidas()
        os.system("cls")
# Totais
    elif escolha == 3:
        os.system("cls")
        
    else:
        print("Escolha uma das opções validas acima.")
