# Importa os módulos necessários
import json  # Para trabalhar com arquivos JSON
import os    # Para manipulação de caminhos de arquivos no sistema operacional

# Define o nome do arquivo JSON que será criado/lido
NOME_ARQUIVO = 'aula177.json'

# Cria o caminho absoluto do arquivo com base no local onde o script está sendo executado
# Isso garante que o arquivo seja salvo/lido corretamente, mesmo em sistemas diferentes
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),  # Pega o diretório atual do arquivo Python
        NOME_ARQUIVO                # Junta com o nome do arquivo desejado
    )
)

# Dicionário representando um filme, que será convertido em JSON
filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,  # Indica que é um filme
    'imdb_rating': 8.8,  # Nota no IMDb
    'year': 2001,  # Ano de lançamento
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],  # Lista de personagens
    'budget': None  # Orçamento indefinido (None será convertido em null no JSON)
}

# Abre (ou cria) o arquivo JSON em modo de escrita ('w') e escreve o dicionário nele
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    # Serializa (converte) o dicionário 'filme' para o formato JSON e salva no arquivo
    # ensure_ascii=False mantém os acentos/acentuação
    # indent=2 deixa o JSON "bonitinho" (identado com 2 espaços)
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

# Abre o mesmo arquivo em modo de leitura ('r') para ler os dados
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    # Lê o conteúdo do arquivo JSON e desserializa (converte) de volta para um dicionário Python
    filme_do_json = json.load(arquivo)
    # Exibe o dicionário carregado na tela
    print(filme_do_json)
