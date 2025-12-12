# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

# Importa o módulo locale, usado para formatação de moeda e outros dados locais
import locale

# Importa o módulo string, que contém a classe Template usada para substituição de variáveis em texto
import string

# Importa a classe datetime para manipular datas
from datetime import datetime

# Importa a classe Path para trabalhar com caminhos de arquivos de forma mais simples e moderna
from pathlib import Path

# Define o caminho do arquivo de texto que será usado como base para o template
# `__file__` representa o caminho do próprio script Python
CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183.txt'

# Define a localidade (idioma e formato cultural) do sistema, neste caso a localidade padrão do sistema operacional
# Isso influencia, por exemplo, como moedas e datas são formatadas
locale.setlocale(locale.LC_ALL, '')

# Função que recebe um número float e retorna ele formatado como moeda brasileira (BRL)
def converte_para_brl(numero: float) -> str:
    # Formata o número como moeda brasileira sem o símbolo (com separadores de milhar)
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl

# Cria um objeto datetime com uma data específica
data = datetime(2022, 12, 28)

# Cria um dicionário com os dados que serão usados para preencher o template de texto
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),  # Valor formatado como moeda BRL
    data=data.strftime('%d/%m/%Y'),      # Data formatada como string no formato brasileiro
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)


#NÃO É RECOMENDADO, MAS SE PRECISAR FAÇA ISSO:
# Cria uma subclasse personalizada de string.Template para trocar o delimitador padrão ($) por %
class MyTemplate(string.Template):
    delimiter = '%'



# Abre o arquivo de texto onde está o conteúdo do template, no modo de leitura
with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()                   # Lê todo o conteúdo do arquivo como string
    template = MyTemplate(texto)             # Cria um objeto template usando o conteúdo do arquivo
    print(template.substitute(dados))        # Substitui as variáveis do texto pelos valores no dicionário e imprime o resultado
