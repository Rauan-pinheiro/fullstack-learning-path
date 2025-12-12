# O módulo os para interação com o sistema
# Doc: https://docs.python.org/3/library/os.html
# O módulo `os` fornece funções para interagir com o sistema operacional.
# Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de
# arquivos e a função os.listdir() pode ser usada para listar os arquivos em um
# diretório. O método os.system() permite executar comandos do sistema
# operacional a partir do seu código Python.
# Windows 11 (PowerShell), Linux, Mac = clear
# Windows (antigo, cmd) = cls
import os
import time

# os.system('echo "Hello world"')

# print('a' * 80)
# print('a' * 80)
# print('a' * 80)
# print('a' * 80)
# print('a' * 80)
# print('a' * 80)

# time.sleep(3)

# os.system('cls')

# print('Tudo limpo')

#uma maneira de encontrar o caminho do arquivo/diretório
caminho = os.path.abspath("dadosPOO.json")
print()
print(caminho)
print()

#outra maneira (local)
caminho_2 = os.getcwd()
print()
print(caminho_2)
print()
