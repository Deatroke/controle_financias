import os
import subprocess
import ctypes

# Verifica o sistema operacional
sistema_operacional = os.name

# Pega o caminho da pasta atual
caminho_pasta = os.path.dirname(os.path.abspath(__file__))

# Verifica qual comando usar para abrir o terminal/cmd como administrador
if sistema_operacional == 'nt':  # Windows
    comando = ['cmd', '/k', f'cd /d "{caminho_pasta}" && python index.py']  # Comando para abrir o cmd e executar o arquivo Python
else:  # macOS/Linux
    comando = ['gnome-terminal', '--', 'python', 'index.py']  # Comando para abrir o terminal e executar o arquivo Python

# Abre o terminal/cmd como administrador e executa o comando
if sistema_operacional == 'nt':  # Windows
    if ctypes.windll.shell32.IsUserAnAdmin():  # Verifica se o usuário atual já possui privilégios de administrador
        subprocess.Popen(['start'] + comando, shell=True)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd", ' '.join(comando), None, 1)
else:  # macOS/Linux
    subprocess.Popen(comando)
