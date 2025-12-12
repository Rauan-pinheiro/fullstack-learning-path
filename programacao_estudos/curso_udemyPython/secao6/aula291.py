# Manipulando caminhos, pastas e arquivos no python com pathlib
from pathlib import Path
from shutil import rmtree 

# principais comandos:
# path.absolute()
# path.parent
# path.home()
# .touch()
# write_text
# .unlink
# mkdir
# .read_text
# .write
# .rmdir() usado para apagr diretórios(se estiver vazio)

project_path = Path()

#Caminho até a primeira pasta criada
print('.'*20)
print(project_path.absolute())
print('.'*20)

#Caminho onde esse aruivo diretamente está (aula291.py)
project_path = Path(__file__)
print('.'*20)
print(project_path)
print('.'*20)

#Ver a pasta mãe (se quiser olhar quem está acima da pasta, na frente de ".parent", adicione outro ".parent")
print(project_path.parent)
print('.'*20)

#Mostra a pasta mãe(posso determinar o nome do diretório da pasta)
ideas = project_path.parent / 'ideas'
print(ideas)

#Obetendo o caminho da pasta pessoal do usuário(home)
caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
#Esse comando abaixo cria o arquivo no caminho que eu passei.
caminho_arquivo.touch()
# print(arquivo)
caminho_arquivo.write_text("Olá, mundo!") #Escrever dentro do arquivo
# print(arquivo.read_text()) #Ler o conteúdo do arquivo
caminho_arquivo.unlink()

# with open(caminho_arquivo, 'a+') as file:
#     file.write("uma linha \n")
#     file.write("outra linha \n")
# print(caminho_arquivo.read_text())

caminho_pasta = Path.home() / 'Desktop' / '4r_midia_teste'
caminho_pasta.mkdir(exist_ok= True) # "mkdir" usado para criar uma pasta(cria uma pasta "4r_midia_teste" no caminho)
# "exist_ok = True" serve para evitar um transtorno, se executar mais de uma o computador vai dar um error dizendo que já existe essa pasta, com o "exist_ok = True" ele apenas ignora o erro, relaxa, não faz nada.
sub_pasta = caminho_pasta / 'sub_pasta' # Dentro da pasta "4r_midia_teste" ele vai criar outra pasta chamada "sub_pasta"
sub_pasta.mkdir(exist_ok=True)

outro_arquivo = sub_pasta / 'arquivo.txt' #Dentro de sub_pasta agora existe um arquivo .txt
outro_arquivo.touch()
outro_arquivo.write_text('hey')

mais_arquivo = caminho_pasta / 'arquivo.txt' #Na mesma pasta sub_pasta existe um arquivo .txt
mais_arquivo.touch()
mais_arquivo.write_text('hey')

rmtree(caminho_pasta)